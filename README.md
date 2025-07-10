



* The file `prayer_leiden.json` is a full export of the Heurist database that was created for the Pages of Prayer project. This expor is in the JSON format. 
* `Texts_in_books.ipynb` converts this export file into a JSON file listing the book and the texts contained with these books. Books and texts are identified using Heurist IDs. During this conversion, some texts are also removed from the dataset. As the focus is primarily on prayers, the ‘standard’ texts of the Book of Hours in Grote’s translation, the calendars, computational tables, circles and figures have been discarded. A number of texts, such as the five variants of G004, Prayers of St. Gregory to the Arma Christi, have been merged. The notebook can extract manuscript books and printed books separately. The output is saved as 'manuscript_books.json' or 'print_books.json', depending on the value set for the of the `book_type` variable. 
* The notebook named `Clusters_random_order.ipynb` calculates the Pairwise Mutual Information score for each set of texts in the dataset. Additionally, it establishes the groupings each text is part of. For each text,all the associated texts are found by identifying the texts that are linked to the source text on the basis of a positive PMI score. 
* The notebook named `Book_similarity_text_order_disregarded.ipynb` examines the simulaties between books on the basis of cosine similarity. 



