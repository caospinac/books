import requests


def self_link(id):
    return "https://www.googleapis.com/books/v1/volumes/" + id


def info_link(id):
    return "http://books.google.com/books?id=" + id


def thumbnail_link(id, edge=False):
    return "http://books.google.com/books/content?\
id={}&printsec=frontcover&img=1&zoom=1&{}source=gbs_api"\
.format(id, "edge=curl&" if edge else "")


def short_description(text):
    if len(text) >= 365:
        return text[:365] + "..."
    return text


def search(
    query, start_index=0, max_results=40, free_only=True, order_by="relevance"
):
    res = dict()
    parms = {
        "printType": "books",
        "filter": "free-ebooks" if free_only else "full",
        "q": query,
        "startIndex": start_index,
        "maxResults": max_results,
        "orderBy": order_by
    }
    r = requests.get(
        url="https://www.googleapis.com/books/v1/volumes", params=parms
    )
    rj = r.json()
    res.update(dict(query=query, count=rj["totalItems"], items=[]))
    for item in rj["items"]:
        try:
            id = item["id"]
            vol_info = item["volumeInfo"]
            new = dict(
                id=id,
                title=vol_info["title"],
                subtitle=None,
                authors='; '.join(vol_info["authors"]),
                short_description=short_description(vol_info["description"]),
                categories='; '.join(vol_info["categories"]),
                thumbnail_link=thumbnail_link(id),
                download_link=None,
                description="Description is not available"
            )
            if "downloadLink" in item["accessInfo"]["pdf"]:
                new["download_link"] = item[
                    "accessInfo"]["pdf"]["downloadLink"]
            if "description" in item["volumeInfo"]:
                new["description"] = item["volumeInfo"]["description"]
            if "subtitle" in item["volumeInfo"]:
                new["subtitle"] = item["volumeInfo"]["subtitle"]
            res["items"].append(new)
        except KeyError as e:
            pass
    return res


def book(id):
    r = requests.get(url=self_link(id))
    return repr(r.json())
