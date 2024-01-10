#input_folder_path = "../../DATA/TestSetAngles"
#output_folder_path = "../../DATA MODIFIED/AlphaAngles_OutputTest" wtf c'est pas possible !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

input_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/TestSetAngles"
output_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/AlphaAngles_OutputTest"

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for filename in os.listdir(input_folder_path):
    if filename.endswith(".json"):
        filepath = os.path.join(input_folder_path, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
        for protein_name, protein_data in data.items():
            alpha_angles = protein_data["angles"]["alpha"]
            sequence = protein_data["sequence"]
            alpha_data = {"alpha": alpha_angles, "sequence": sequence}
            output_filepath = os.path.join(output_folder_path, f"{protein_name}_alpha_angles.json")
            with open(output_filepath, 'w') as output_file:
                json.dump({protein_name: alpha_data}, output_file, indent=2)

            print(f"Angles alpha et séquence pour {protein_name} enregistrés dans {output_filepath}")



def sequence_to_one_hot(sequence, max_length):
    num_nucleotides = 4
    one_hot_matrix = np.zeros((max_length, num_nucleotides), dtype=int)

    for i, nucleotide in enumerate(sequence):
        if nucleotide == 'A':
            one_hot_matrix[i, 0] = 1
        elif nucleotide == 'C':
            one_hot_matrix[i, 1] = 1
        elif nucleotide == 'G':
            one_hot_matrix[i, 2] = 1
        elif nucleotide == 'U':
            one_hot_matrix[i, 3] = 1

    return one_hot_matrix

#folder_path = "../../DATA MODIFIED/AlphaAngles_OutputTest"
#output_folder_path = "../../DATA MODIFIED/OneHotMatrices_OutputTest"

folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/AlphaAngles_OutputTest"
output_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/OneHotMatrices_OutputTest"

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

max_length = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
        for protein_name, protein_data in data.items():
            sequence = protein_data.get("sequence", "")
            max_length = max(max_length, len(sequence))

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
        for protein_name, protein_data in data.items():
            sequence = protein_data.get("sequence", "")
            
            if len(sequence) < max_length:
                one_hot_matrix = sequence_to_one_hot(sequence, max_length)
            else:
                one_hot_matrix = sequence_to_one_hot(sequence, len(sequence))

            output_filepath = os.path.join(output_folder_path, f"{protein_name}_one_hot_matrix.npy")
            np.save(output_filepath, one_hot_matrix)

            print(f"Matrice one-hot encoded pour {protein_name} dans {filename} enregistrée dans {output_filepath}")

#output_folder_path = "../../DATA MODIFIED/OneHotMatrices_OutputTest"

output_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/OneHotMatrices_OutputTest"
for filename in os.listdir(output_folder_path):
    if filename.endswith("_one_hot_matrix.npy"):
        filepath = os.path.join(output_folder_path, filename)
        one_hot_matrix = np.load(filepath)

        print(f"Matrice one-hot encoded chargée depuis {filename}:")
        print(one_hot_matrix)
