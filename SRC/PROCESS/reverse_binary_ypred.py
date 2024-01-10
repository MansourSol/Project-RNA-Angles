import os

def process_file(input_file, output_folder):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        results = [61.5 if int(classe) == 2 else 0 if int(classe) == 0 else -118.5 for classe in lines]
        results_padded = results + [0] * (188 - len(results))

        output_file = os.path.join(output_folder, os.path.basename(input_file))

        with open(output_file, 'w') as f_dest:
            for result in results_padded:
                f_dest.write(str(result) + '\n')

        print(f"Results for the file {input_file} have been saved to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    #input_file_path = "../../RESULTS/PREDICTION_SAMPLE/example_pred.txt" 
    #output_folder_path = "../../RESULTS/PREDICTION_SAMPLE/Reverse_TestBinaireExample"
    
    input_file_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/sample/example_pred.txt"
    output_folder_path = "/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/Reverse_TestBinaireExample"
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    process_file(input_file_path, output_folder_path)
