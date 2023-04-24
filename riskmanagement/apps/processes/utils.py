def update_process_tree_types(parent_process, updated_process_type):
    # Changing the process's type
    print('inside')
    print(parent_process.title + ' ' + updated_process_type.name)
    parent_process.process_type = updated_process_type
    parent_process.save()
    print('success')

    # Getting the type that we must assign to the process's children
    children_process_types = updated_process_type.get_children()
    

    if(len(children_process_types) > 0):
        updated_children_type = children_process_types[0]
        print(updated_children_type)
        # Update the current process's children type
        for child_process in parent_process.get_children():
            update_process_tree_types(child_process, updated_children_type)
    else:
        # Delete all the children because we don't have a type to assign
        for child_process in parent_process.get_children():
            child_process.delete()
