import hashlib


class ConsistentHashing:
    def __init__(self, num_slots=512):
        """
        Initialize the ConsistentHashing class.

        Parameters:
        num_slots (int): The number of slots in the hash ring. Default is 512.
        """
        self.num_slots = num_slots
        self.nodes = []  # List to store the nodes and their virtual replicas

    def _hash_virtual(self, node, replica):
        """
        Generate a hash value for a virtual replica of a node.

        Parameters:
        node (str): The identifier of the physical node.
        replica (int): The replica number of the node.

        Returns:
        int: The hashed key value.
        """
        # Convert the node identifier to a hash value using MD5
        node_hash = int(hashlib.md5(node.encode("utf-8")).hexdigest(), 16)
        # Calculate the position of the virtual node on the hash ring
        return (node_hash**2 + replica**2 + 2 * replica + 25) % self.num_slots
