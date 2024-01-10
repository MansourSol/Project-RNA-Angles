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

example_folder_path = "../../DATA/sample"
output_folder_path = "../../DATA/sample/OneHotMatrices_OutputExample"   

#example_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/sample"
#output_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/sample/OneHotMatrices_OutputExample"

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

max_length_training = 395
for filename in os.listdir(example_folder_path):
    if filename.endswith(".fasta"):
        filepath = os.path.join(example_folder_path, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            sequence = "".join(line.strip() for line in lines[1:])
            max_length_training = max(max_length_training, len(sequence))
for filename in os.listdir(example_folder_path):
    if filename.endswith(".fasta"):
        filepath = os.path.join(example_folder_path, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            sequence = "".join(line.strip() for line in lines[1:])
            if len(sequence) < max_length_training:
                one_hot_matrix = sequence_to_one_hot(sequence, max_length_training)
            else:
                one_hot_matrix = sequence_to_one_hot(sequence, len(sequence))

            output_filepath = os.path.join(output_folder_path, f"{filename.split('.')[0]}_one_hot_matrix.npy")
            np.save(output_filepath, one_hot_matrix)

            print(f"Matrice one-hot encodée pour {filename} enregistrée dans {output_filepath}")

output_folder_path = "../../DATA/sample/OneHotMatrices_OutputExample"

#output_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/sample/OneHotMatrices_OutputExample"
for filename in os.listdir(output_folder_path):
    if filename.endswith("_one_hot_matrix.npy"):
        filepath = os.path.join(output_folder_path, filename)
        one_hot_matrix = np.load(filepath)

        print(f"Matrice one-hot encoded chargée depuis {filename}:")
        print(one_hot_matrix)
