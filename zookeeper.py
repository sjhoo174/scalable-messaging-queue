from kazoo.client import KazooClient

# Connect to the Zookeeper server (replace with your Zookeeper server address)
zk_host = 'localhost:2181'  # Zookeeper address
zk = KazooClient(hosts=zk_host)

# Connect to the Zookeeper ensemble
zk.start()

def list_nodes(path='/'):
    """Recursive function to list all znodes and their data in Zookeeper."""
    try:
        # Get children nodes of the given path
        children = zk.get_children(path)
        print(f"Nodes at {path}: {children}")
        
        # Recursively list children of each child node
        for child in children:
            full_path = f"{path}/{child}"
            # Get the data of the node (this will return a tuple: (data, stat))
            data, stat = zk.get(full_path)
            print(f"Data at {full_path}: {data.decode('utf-8') if data else None}")  # Decode if data exists
            
            # Recurse into child node
            list_nodes(full_path)  # Recurse into child node

    except Exception as e:
        print(f"Error listing nodes under path {path}: {e}")

# List all znodes starting from root '/'
list_nodes('/')

# Close the connection to Zookeeper
zk.stop()