"""
    Create an API server for drink data. Use the 'cocktails.json' file as the source of data for your server. Your server should have the following endpoints and behaviors:

    /search
        This API endpoint accepts a query parameter 's', that allows the user to search all drinks for drink names that match the word(s) provided in 's'. Multiple search terms can be provided as a comma separated list of terms and the search should match on names including any of those terms. This returns an array of matching drink names and respective ids.
    /ingredients
        This API endpoint accepts a query parameter 's', that allows the user to search all drinks for drink ingredients that match the word(s) provided in 's'. Multiple search terms can be provided as a comma separated list of terms and the search should match on ingredients including any of those terms. This returns an array of matching drink names and respective ids.
    /details/<drink_id>
        This API endpoint uses the path parameter to find a specific drink and returns all the details of that drink.

    Then create a UI that uses the API server above to give the user the ability to search by drink name or particular ingredients. (Two different forms, please.) Once the user receives a list of matches from either one of the searches, clicking on one of the matches will provide all the details of that drink on another page in an attractive way.
"""