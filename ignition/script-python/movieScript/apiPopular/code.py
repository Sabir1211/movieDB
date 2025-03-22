def apiPopular(page):
    """ This function returns a list of movie instances from the TMDb API based on the page number. """
    try:
        # API URL and Headers
        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=" + str(page)
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNTcyMTU2ZDQ3YjllM2U0M2RhMjA0MDRhMDQwYzNhOCIsIm5iZiI6MTczNjIyMzM0My44MjksInN1YiI6IjY3N2NhYTZmZDEwMmU3NzZmNTc0ODhiYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nwAHnyYb8Ej1UCswTkltuNKZsCWWeknfHz_6Y0oi2es"  # Replace with your token (don't hardcode in production)
        }

        # Create an HTTP client (assuming this is a platform-specific function)
        http_client = system.net.httpClient()
        response = http_client.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.getStatusCode() == 200:
            # Decode the JSON response
            result = system.util.jsonDecode(response.getText())
            movies = result.get("results", [])
            total_pages = result.get("total_pages", "")

            # Create instances list dynamically
            instances = []
            for movie in movies:
                # Handle the case when 'poster_path' is missing or empty
                poster_path = movie.get("poster_path", "")
                img_url = "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else "default_image_url.jpg"

                instance = {
                    "viewPath": "New Folder/tmpMovie",  # The path to your embedded view
                    "params": {
                        "title": movie.get("title", "Unknown Title"),
                        "imgPath": img_url,
                        "rate": movie.get("vote_average", "N/A"),
                        "id" :int( movie.get("id", "N/A")),
                        
                    }
                }
                
                instances.append(instance)
            instances.append({"total_pages" : total_pages})
            return instances
        else:
            print "Failed to fetch data: %d" % response.getStatusCode()  # Print error status code
            return []
    except Exception as e:
        print "Error: %s" % str(e)  # Log or print the error message for debugging
        return []
