from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        """
        Find all words from queries that can be matched with at least one word 
        in dictionary with at most 2 character differences.
      
        Args:
            queries: List of query strings to check
            dictionary: List of reference strings to compare against
          
        Returns:
            List of query strings that have at least one dictionary match 
            with 2 or fewer character differences
        """
        result = []
      
        # Check each query word
        for query_word in queries:
            # Try to find a matching word in the dictionary
            for dict_word in dictionary:
                # Count the number of differing characters at the same positions
                differences = sum(char_q != char_d 
                                for char_q, char_d in zip(query_word, dict_word))
              
                # If differences are at most 2, add query word to result
                if differences <= 2:
                    result.append(query_word)
                    break  # Found a match, no need to check other dictionary words
                  
        return result      