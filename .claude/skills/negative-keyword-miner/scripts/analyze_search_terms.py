#!/usr/bin/env python3
"""
Negative Keyword Miner - Analysis Script
Analyzes search term report CSV and identifies negative keyword opportunities
"""

import csv
import sys
from collections import defaultdict
from typing import List, Dict, Tuple
import re

class NegativeKeywordAnalyzer:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file
        self.search_terms = []
        self.zero_converters = []
        self.high_cost_low_performance = []
        self.patterns = defaultdict(list)
        
        # Common negative keyword patterns
        self.universal_patterns = {
            'jobs': ['jobs', 'career', 'careers', 'hiring', 'salary', 'employment'],
            'free': ['free', 'no cost', 'without paying'],
            'diy': ['diy', 'how to make', 'homemade', 'build yourself'],
            'academic': ['thesis', 'dissertation', 'homework', 'assignment', 'student project'],
            'info': ['definition', 'meaning', 'what is', 'explained'],
            'media': ['images', 'wallpaper', 'clipart', 'png', 'logo'],
            'downloads': ['pdf download', 'template download', 'free download'],
        }
    
    def load_csv(self):
        """Load and parse CSV file"""
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    term_data = {
                        'term': row.get('Search Term', '').lower().strip(),
                        'impressions': int(row.get('Impressions', 0)),
                        'clicks': int(row.get('Clicks', 0)),
                        'cost': float(row.get('Cost', '0').replace('$', '').replace(',', '')),
                        'conversions': int(row.get('Conversions', 0)),
                    }
                    
                    if term_data['clicks'] > 0:  # Only analyze terms with clicks
                        self.search_terms.append(term_data)
            
            print(f"✓ Loaded {len(self.search_terms)} search terms with clicks")
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file}' not found")
            return False
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False
    
    def identify_zero_converters(self):
        """Find search terms with clicks but zero conversions"""
        for term in self.search_terms:
            if term['conversions'] == 0 and term['cost'] > 0:
                self.zero_converters.append(term)
        
        # Sort by cost (highest first)
        self.zero_converters.sort(key=lambda x: x['cost'], reverse=True)
        print(f"✓ Found {len(self.zero_converters)} zero-conversion terms")
    
    def detect_patterns(self):
        """Detect common negative keyword patterns"""
        for term_data in self.zero_converters:
            term = term_data['term']
            
            # Check universal patterns
            for pattern_name, keywords in self.universal_patterns.items():
                for keyword in keywords:
                    if keyword in term:
                        self.patterns[pattern_name].append(term_data)
                        break
        
        print(f"✓ Detected {len(self.patterns)} pattern categories")
    
    def calculate_pattern_costs(self) -> List[Tuple[str, float, int]]:
        """Calculate total cost for each pattern"""
        pattern_costs = []
        
        for pattern_name, terms in self.patterns.items():
            total_cost = sum(t['cost'] for t in terms)
            term_count = len(terms)
            pattern_costs.append((pattern_name, total_cost, term_count))
        
        # Sort by cost (highest first)
        pattern_costs.sort(key=lambda x: x[1], reverse=True)
        return pattern_costs
    
    def extract_common_words(self) -> Dict[str, Tuple[int, float]]:
        """Extract most common words in zero-conversion terms"""
        word_stats = defaultdict(lambda: {'count': 0, 'cost': 0.0})
        
        # Common words to ignore (too generic)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                     'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be'}
        
        for term_data in self.zero_converters:
            words = re.findall(r'\b\w+\b', term_data['term'].lower())
            for word in words:
                if word not in stop_words and len(word) > 2:
                    word_stats[word]['count'] += 1
                    word_stats[word]['cost'] += term_data['cost']
        
        # Convert to list and sort by cost
        word_list = [(word, stats['count'], stats['cost']) 
                     for word, stats in word_stats.items()]
        word_list.sort(key=lambda x: x[2], reverse=True)
        
        return word_list[:20]  # Top 20
    
    def generate_report(self):
        """Generate analysis report"""
        total_cost = sum(t['cost'] for t in self.search_terms)
        wasted_cost = sum(t['cost'] for t in self.zero_converters)
        waste_percentage = (wasted_cost / total_cost * 100) if total_cost > 0 else 0
        
        print("\n" + "="*70)
        print("NEGATIVE KEYWORD ANALYSIS REPORT")
        print("="*70)
        
        print(f"\n📊 SUMMARY")
        print(f"   Total Search Terms Analyzed: {len(self.search_terms)}")
        print(f"   Total Ad Spend: ${total_cost:,.2f}")
        print(f"   Zero-Conversion Terms: {len(self.zero_converters)}")
        print(f"   Wasted Spend: ${wasted_cost:,.2f} ({waste_percentage:.1f}%)")
        print(f"   Potential Monthly Savings: ${wasted_cost * 0.95:,.2f}")
        
        print(f"\n🚨 TOP 10 HIGHEST-COST ZERO CONVERTERS")
        print(f"{'Search Term':<50} {'Cost':>12}")
        print("-" * 70)
        for term in self.zero_converters[:10]:
            print(f"{term['term'][:50]:<50} ${term['cost']:>10,.2f}")
        
        print(f"\n🔍 PATTERN ANALYSIS")
        pattern_costs = self.calculate_pattern_costs()
        for pattern_name, cost, count in pattern_costs:
            print(f"   {pattern_name.upper():15} - ${cost:>8,.2f} ({count} terms)")
        
        print(f"\n💬 TOP RECURRING WORDS IN WASTED SEARCHES")
        common_words = self.extract_common_words()
        for word, count, cost in common_words[:10]:
            print(f"   '{word}' - {count} occurrences, ${cost:,.2f} wasted")
        
        print(f"\n✅ RECOMMENDED IMMEDIATE NEGATIVES (TIER 1)")
        
        # Pattern-based recommendations
        pattern_costs = self.calculate_pattern_costs()
        for pattern_name, cost, count in pattern_costs[:5]:
            if cost > 50:  # Only recommend if significant cost
                keywords = self.universal_patterns.get(pattern_name, [])
                print(f"\n   Pattern: {pattern_name.upper()} (${cost:,.2f} waste)")
                for kw in keywords[:3]:  # Top 3 keywords for this pattern
                    print(f"      - Add '{kw}' as Broad Match Negative")
        
        # Individual term recommendations
        print(f"\n   High-Cost Individual Terms:")
        for term in self.zero_converters[:5]:
            if term['cost'] > 100:
                print(f"      - Add '{term['term']}' as Exact Match Negative (${term['cost']:,.2f})")
        
        print(f"\n📋 NEXT STEPS")
        print(f"   1. Review recommended negatives above")
        print(f"   2. Add Tier 1 negatives to your ad account")
        print(f"   3. Monitor impressions for 3-7 days")
        print(f"   4. Export new search terms report and re-run analysis")
        print(f"   5. Expected savings: ${wasted_cost * 0.7:,.2f} - ${wasted_cost * 0.9:,.2f}/month")
        
        print("\n" + "="*70)
    
    def run_analysis(self):
        """Run complete analysis"""
        if not self.load_csv():
            return False
        
        self.identify_zero_converters()
        self.detect_patterns()
        self.generate_report()
        
        return True


def main():
    """Main execution"""
    if len(sys.argv) < 2:
        print("Usage: python negative_keyword_analyzer.py <search_terms_report.csv>")
        print("\nCSV should contain columns:")
        print("  - Search Term")
        print("  - Impressions")
        print("  - Clicks")
        print("  - Cost")
        print("  - Conversions")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    print("🔍 Starting Negative Keyword Analysis...")
    print(f"📁 File: {csv_file}\n")
    
    analyzer = NegativeKeywordAnalyzer(csv_file)
    
    if analyzer.run_analysis():
        print("\n✅ Analysis complete!")
        print("\nℹ️  For detailed recommendations with match types and priority tiers,")
        print("   provide this data to the Negative Keyword Miner Claude Skill.")
    else:
        print("\n❌ Analysis failed. Please check the CSV file format.")
        sys.exit(1)


if __name__ == "__main__":
    main()
