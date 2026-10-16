import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Practical 9: Network Routing Diagram from Router Data
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, 'sample2.csv')

print("--- Network Routing Diagram ---")

try:
    df = pd.read_csv(csv_file)
    print("Loaded Router Data:")
    print(df)
except FileNotFoundError:
    print("Error: 'sample2.csv' not found. Please create the file.")
    df = pd.DataFrame()

if not df.empty:
    G = nx.from_pandas_edgelist(df, 'source', 'target')
    print("\nGraph created successfully.")
    print(f"Number of nodes (routers): {G.number_of_nodes()}")
    print(f"Number of edges (connections): {G.number_of_edges()}")

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.9, iterations=50, seed=42)

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000,
            edge_color='gray', font_size=12, font_weight='bold')

    plt.title("Network Routing Diagram", size=16)

    # Save output plot image
    output_image = os.path.join(BASE_DIR, 'network_routing_output.png')
    plt.savefig(output_image, dpi=200, bbox_inches='tight')
    print(f"Diagram image saved to: {output_image}")

    # Display plot window (in IDLE, closing window completes the script)
    if os.environ.get("NO_SHOW") != "1":
        print("\nDisplaying diagram window... (close window to finish)")
        plt.show()
else:
    print("\nCould not generate diagram due to missing data.")

print("\n--- Network Diagram Complete ---")
