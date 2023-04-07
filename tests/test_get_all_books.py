from requests_folder.get_all_books import get_all_books

class TestBooks:
    def test_get_all_books_no_filter_no_type_check_status_code(self):
        r = get_all_books("","")
        assert r.status_code == 200, f"Error: status code not good. Expected 200, actual: {r.status_code}"
    def test_get_all_books_no_filter_no_type_check_nr_rez(self):
        r=get_all_books("","")
        assert len(r.json())==6, f"Error: Expected 6, actual {len(r.json())}"
    def test_get_all_books_type_ficition(self):
        r=get_all_books("fiction","").json()
        assert len(r)==4, f"Error: Expected 4, actual {len(r)}"
        for i in range(len(r)):
            assert r[i]["type"]=="fiction", f"Error Book{r[i]['name']} has an invalid type"
    def test_get_all_books_type_nonficition(self):
        r=get_all_books("non-fiction","").json()
        assert len(r)==2, f"Error: Expected 2, actual {len(r)}"
        for i in range(len(r)):
            assert r[i]["type"]=="non-fiction", f"Error Book{r[i]['name']} has an invalid type"
    def test_get_all_books_type_invalid(self):
        r=get_all_books("pepelepe","")
        assert r.status_code == 400, f"Error: status code not good. Expected 400, actual: {r.status_code}"
        assert r.json()["error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_get_all_books_no_type_negative_limit(self):
        r = get_all_books( "", "-7" )
        assert r.status_code == 400, f"Error: status code not good. Expected 400, actual: {r.status_code}"
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0.", f"Error:Wrong message: {r.json()['error']}"

    def test_get_all_books_limit_invalid(self):
        r = get_all_books("fiction","25")
        assert r.status_code == 400
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", f"Error is not corect. Message is {r.json()['error']}"



