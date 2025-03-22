def apiMovieDetails(movieID):
    """ This function returns a list of movie instances from the TMDb API based on the page number. """
    try:
        # API URL and Headers
        url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movieID)
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNTcyMTU2ZDQ3YjllM2U0M2RhMjA0MDRhMDQwYzNhOCIsIm5iZiI6MTczNjIyMzM0My44MjksInN1YiI6IjY3N2NhYTZmZDEwMmU3NzZmNTc0ODhiYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nwAHnyYb8Ej1UCswTkltuNKZsCWWeknfHz_6Y0oi2es"  # Replace with your token (don't hardcode in production)
        }

        # Create an HTTP client (assuming this is a platform-specific function)
        http_client = system.net.httpClient()
        response = http_client.get(url, headers=headers)
#        print response.getStatusCode()
        # Check if the request was successful (status code 200)
        if response.getStatusCode() == 200:
            # Decode the JSON response
            result = system.util.jsonDecode(response.getText())
            movies = [result]
#            movies = result.get("results", [])
			
            # Create instances list dynamically
            instances = []
            for movie in movies:
            	
                # Handle the case when 'poster_path' is missing or empty
                poster_path = movie.get("backdrop_path", "")
                backdrop_path = movie.get("backdrop_path", "NA")
                img_url = "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else "default_image_url.jpg"
                bg_url = "https://image.tmdb.org/t/p/w500/" + backdrop_path if backdrop_path else "default_image_url.jpg"
                instances = [genre["name"] for genre in movie.get("genres", "")]
#                print geners

                instance = {
                    "viewPath": "New Folder/tmpMovieDetails",  # The path to your embedded view
                    "params": {
                        "id" : movie.get("id", "N/A"),
                        "genres" : ", ".join(instances),
                        "original_title" : movie.get("original_title", "N/A"),
                        "overview" : movie.get("overview", "N/A"),
                        "release_date" :str( movie.get("release_date", "N/A")),
                        "runtime" : movie.get("runtime", "N/A"),
                        "vote_average" : movie.get("vote_average", "N/A"),
                         "imgPath": img_url,
                         "bgPath":bg_url
                    }
                }
#                instances.append(instance)

            return instance
        else:
            print "Failed to fetch data: %d" % response.getStatusCode()  # Print error status code
            return []
    except Exception as e:
        print "Error: %s" % str(e)  # Log or print the error message for debugging
        return []