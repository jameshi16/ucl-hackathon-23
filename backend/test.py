input_string = "1. Classes and Objects: \"Classes and Objects tutorial\"\n2. Encapsulation: \"Encapsulation in OOP explained\"\n3. Inheritance: \"Inheritance in OOP tutorial\"\n4. Polymorphism: \"Polymorphism in OOP made easy\"\n5. Abstraction: \"Abstraction in OOP tutorial\"\n6. Interfaces: \"Interfaces in OOP explained\"\n7. Composition: \"Composition in OOP tutorial\"\n8. Design Patterns: \"Design patterns in OOP explained\"\n9. SOLID Principles: \"SOLID Principles tutorial\"\n10. Testing: \"Testing in OOP tutorial\""

subtopics_dict = {}

# Split the input string into lines
lines = input_string.split('\n')

# Loop through the lines and extract the subtopic and search term for each one
for line in lines:
    if line.strip() == "" or line[0].isdigit() == False:
        continue
    subtopic, search_term = line.split(": ")
    subtopic_num, subtopic_name = subtopic.split(". ")
    subtopics_dict[subtopic_name] = [search_term.strip('"')]

print(subtopics_dict)