import sys, requests, fire, json

server = "https://rest.ensembl.org"
exp_message = "\nExport output?\nIf Yes, it will overwrite output.json\nY or N\n"

def GET_tax_id(id):
    """
    Search for a taxonomic term by its identifier or name
        | id: NCBI taxon id or a name
    """
    ext = "/taxonomy/id/"
    exp = None
    url = server + ext + str(id) + "?"
    r = requests.get(url, headers = {"Content-Type" : "application/json"})

    data = json.loads(r.text)
    
    print(json.dumps(data, indent = 2))
    
    exp = input(exp_message)

    if exp == "Y":
        with open("output.json", "w") as json_f:
            json.dump(data, json_f, indent=2)

def GET_tax_name(name):
    """
    Search for a taxonomic id by a non-scientific name
        | name: A non-scientific species name. Can include SQL wildcards
    """
    ext = "/taxonomy/name/"
    exp = None
    url = server + ext + str(name) + "?"
    r = requests.get(url, headers = {"Content-Type" : "application/json"})

    data = json.loads(r.text)
    
    print(json.dumps(data, indent = 2))
    
    exp = input(exp_message)

    if exp == "Y":
        with open("output.json", "w") as json_f:
            json.dump(data, json_f, indent=2)

if __name__ == "__main__":
    fire.Fire({
        "tax_id" : GET_tax_id,
        "tax_name" : GET_tax_name
    })