def process_resource():
    """Simulate opening a resource and always cleaning up."""
    resource = None
    try:
        resource = open("test.txt", "w")
        resource.write("Hello, World!")
        # Imagine some error might occur here
    finally:
        if resource:
            resource.close()
            print("Resource closed")

# Note: The file is created and closed properly even if an error occurs
process_resource()
