class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        This solution works by grouping words based on common letters
        Therefore I instantiate a hashmap for grouping the words

        The key is a string of sorted letters, while the value is a 
        list of the words having all the letters

        E.g level will belong to the key-value pair

        eellv : ['level']

        tea and eat will belong to:

        aet : ['tea', 'eat']
        '''
        anagrams = dict()

        # Iterate through every word in the list
        for word in strs:
            # Get the string of sorted chars and store in a variable
            '''
            Convert word to list of characters, 
            sort it, then convert to string
            '''
            sorted_word = str(sorted(list(word)))

            # If the string formed by the word is in the string,
            # add it to the list of words having those chars
            if sorted_word in anagrams.keys():
                anagrams[sorted_word].append(word)
            else:
                # Else
                # Not in anagrams
                # Create a new entry for the word on the hashmap
                anagrams[sorted_word] = [word]

        return list(anagrams.values())