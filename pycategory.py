class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        '''Initialize the categories.'''
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], \
        'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
 
    def is_category_valid(self, category_name):
        '''Check if the category is valid.'''
        return self._recur_is_category_valid(self._categories, category_name)

    def _recur_is_category_valid(self, ctgry, category_name):
        '''Recursively check if the category is valid.'''
        if ctgry == None:
            return False
        if type(ctgry) == list:
            for child in ctgry:
                p = self._recur_is_category_valid(child, category_name)
                if p == True:
                    return True
        return ctgry == category_name
 
    def find_subcategories(self, category):
        '''takes a category name to find and'''
        #return self._recur_find_subcategories(category, self._categories)
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:
                if categories == category or found:
                    yield categories

        return list(find_subcategories_gen(category, self._categories))