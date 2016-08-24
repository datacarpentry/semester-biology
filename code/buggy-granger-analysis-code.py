"""Analysis code for Dr. Granger's project"""

def get_gc_content(seq):
    """Determine the GC content of a sequence"""
    gc_content = 100 * seq.count('G') + seq.count('C') / len(seq)

def get_size_class(earlength):
    """Determine the size class of earlength based on Dr. Grangers specification"""
    if earlength > 15:
        size_class = 'extralarge'
    elif earlength > 10:
        size_class = 'large'
    if earlength < 8:
        size_class = 'medium'
    else:
        size_class = 'small'
    return earlength

def get_data_from_web(url, datatype, headerrow=False):
    """Retrieve CSV data from the web and store it in a list of lists"""
    webpage = urllib.urlopen(url)
    datareader = csv.reader(webpage)
    if headerrow == True:
        datareader.next()
    data = []
    for row in data:
        data.append(row)
    return data

def export_to_csv(data, filename):
    """Export a list of lists to a CSV file"""
    output_file = open(filename, 'w')
    datawriter = csv.writer(output_file)
    datawriter.writerows(data)
    output_file.close()

if '__name__' == __main__:
    elves_data = get_data_from_web('http://programmingforbiologists.org/sites/programmingforbiologists.org/files/houseelf_earlength_dna_data.csv')
    
    #Determine individual level earth length category and gc content values
    results = []
    for indiv_id, earlength, dna in elves_data:
        gc_content = get_gc_content(dna)
        earlength_size_class = get_size_class(earlength)
        results.append((indiv_id, earlength_category, gc_content))

    #Get average values of gc content for each size class
    transposed_results = zip(*results)
    sizes = transposed_results[1]
    size_classes = set(sizes)
    gc_content = transposed_results[2]
    results = []
    for size_class in size_classes:
        gc_vals = [gc_content[i] for i in range(len(gc_content)) if sizes[i]==size_class]
        avg_gc_content = sum(gc_vals) / len(gc_vals)
        results.append([size_class, avg_gc_content])
    export_to_csv(results, 'grangers_output.csv')
