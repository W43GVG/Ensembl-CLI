import sys, requests, fire, json, xml

server = "https://rest.ensembl.org"
exp_message = "\nExport output?\nIf Yes, it will overwrite output.json\nY or N\n"

def GET_tax_id(id, format):
    """
    Search for a taxonomic term by its identifier or name
        | id: NCBI taxon id or a name
        | format: either JSON or XML
    """
    ext = "/taxonomy/id/"
    exp = None
    url = server + ext + str(id) + "?"
    
    if format == "json":
        r = requests.get(url, headers = {"Content-Type" : "application/json"})

        data = json.loads(r.text)
        print(json.dumps(data, indent = 2))
        
        exp = input(exp_message)
        if exp == "Y":
            with open("output.json", "w") as json_f:
                json.dump(data, json_f, indent=2)
    elif format == "xml":
        r = requests.get(url, headers = {"Content-Type" : "application/xml"})

        print(r.text)


def GET_tax_name(name, format):
    """
    Search for a taxonomic id by a non-scientific name
        | name: A non-scientific species name. Can include SQL wildcards
        | format: either JSON or XML
    """
    ext = "/taxonomy/name/"
    exp = None
    url = server + ext + str(name) + "?"

    if format == "json":
        r = requests.get(url, headers = {"Content-Type" : "application/json"})

        data = json.loads(r.text)
        print(json.dumps(data, indent = 2))
        
        exp = input(exp_message)
        if exp == "Y":
            with open("output.json", "w") as json_f:
                json.dump(data, json_f, indent=2)
    elif format == "xml":
        r = requests.get(url, headers = {"Content-Type" : "application/xml"})

        print(r.text)

def GET_tax_classification(id, format):
    """
    Return the taxonomic classification of a taxon node
        | id: A taxon identifier. Can be a NCBI taxon id or a name
        | format: either JSON or XML
    """
    ext = "/taxonomy/classification/"
    exp = None
    url = server + ext + str(id) + "?"

    if format == "json":
        r = requests.get(url, headers = {"Content-Type" : "application/json"})

        data = json.loads(r.text)
        print(json.dumps(data, indent = 2))
        
        exp = input(exp_message)
        if exp == "Y":
            with open("output.json", "w") as json_f:
                json.dump(data, json_f, indent=2)
    elif format == "xml":
        r = requests.get(url, headers = {"Content-Type" : "application/xml"})

        print(r.text)

if __name__ == "__main__":
    fire.Fire({
        "tax_id" : GET_tax_id,
        "tax_name" : GET_tax_name,
        "tax_classif" : GET_tax_classification
    })