import json

class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.gpa

    def print_detail(self):
        print(f"ID: {self.std_id}\nName: {self.name}\nGPA: {format(self.gpa, '.2f')}")

class ProbHash:
    def __init__(self, size):
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key):
        return key % self.size

    def rehash(self, hkey):
        return (hkey + 1) % self.size

    def insert_data(self, student):
        key = student.std_id
        hkey = self.hash(key)

        if self.hash_table[hkey] is None:
            self.hash_table[hkey] = student
            print(f"Insert {key} at index {hkey}")
        else:
            i = 1
            while i < self.size:
                new_hkey = self.rehash(hkey)
                if self.hash_table[new_hkey] is None:
                    self.hash_table[new_hkey] = student
                    print(f"Insert {key} at index {new_hkey}")
                    return
                i += 1
                hkey = new_hkey

            print(f"The list is full. {key} could not be inserted.")

    def search_data(self, std_id):
        key = std_id
        hkey = self.hash(key)

        if self.hash_table[hkey] is not None and self.hash_table[hkey].std_id == std_id:
            print(f"Found {std_id} at index {hkey}")
            return self.hash_table[hkey]

        i = 1
        while i < self.size:
            new_hkey = self.rehash(hkey)
            if self.hash_table[new_hkey] is not None and self.hash_table[new_hkey].std_id == std_id:
                print(f"Found {std_id} at index {new_hkey}")
                return self.hash_table[new_hkey]
            i += 1
            hkey = new_hkey

        print(f"{std_id} does not exist.")
        return None


def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()