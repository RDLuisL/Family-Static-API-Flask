
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
   def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
                "id": self._generateId(),
                "first_name": "Jhon",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22] },
# __init__: Este es el constructor de la clase. Inicializa una instancia de la familia con un 
# apellido (last_name) y una lista de miembros iniciales con información de nombre, apellido, 
# edad y números de la suerte.
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3] },

            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1] }]
# _generateId: Este es un método interno utilizado para generar identificadores aleatorios para 
# los miembros. 

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

   # read-only: Use this method to generate random members ID's when adding members into the list
    def add_member(self, member):
        # fill this method and update the return
        pass
# add_member: Este método debe implementarse para agregar un nuevo miembro a la lista _members.
# El nuevo miembro se proporciona como argumento al método.

    def delete_member(self, id):
        # fill this method and update the return
        pass
# delete_member: Este método debe implementarse para eliminar un miembro de la lista _members según 
# el ID proporcionado como argumento.

    def get_member(self, id):
        # fill this method and update the return
        pass
# get_member: Este método debe implementarse para obtener información sobre un miembro específico de
# la familia según el ID proporcionado como argumento.

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
# get_all_members: Este método devuelve la lista completa de miembros de la familia. Ya está implementado 
# y no necesita cambios.