example_one_hot_matrix_path = '../../DATA/sample/OneHotMatrices_OutputExample/example_one_hot_matrix.npy'

#example_one_hot_matrix_path = '/Users/admin-21760/Desktop/M2/Computational Systems and Structural Biology/Bioinformatics of RNA and non-coding world/RNA_angles/RNA-project-angles/data/sample/OneHotMatrices_OutputExample/example_one_hot_matrix.npy'
example_one_hot_matrix = np.load(example_one_hot_matrix_path)
example_normalized = scaler.transform(example_one_hot_matrix)
example_prediction = mlp_binary.predict(example_normalized)

print(f"Prediction for the example sequence: {example_prediction}")
