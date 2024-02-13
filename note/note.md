# Conceptos básicos

## JSON
Es un formato de intercambio de datos estructurados.
Sintaxis:
- Todo objeto va encerrado entre llaves { }.
- Las claves comienzan con comillas " ".
- clave : valor (separadas por una coma):
- Se puede tener varios objetos en una clave pero debe ir entre corchetes [{ }, { }]
- El ultimo dato no debe llevar coma y debe ir en minúscula.

Ejemplos:
```
  {
  	"group" : "Grupo 3",
  	"yeard" : [11,19,23,18]
  }
```
```
{
  "group": "Grupo 7",
  "members" : [
    {
      "name" : "Miguel",
      "last_name" : "Mallqui",
      "country" : "Peru"
    },
    {
      "name": "Juan",
      "last_name": "Perez",
      "country": "Mexico"
    }
  ]
}
```
## Nomenclatura que se utilizara:
- Las clases se escribiran en PascalCase las primera letras en mayúscula.`name` 
- Las variables se escribiran en camelCase la primera letra en minúscula y la primera palbra que le siguie en mayúscula.`endDate`


## Creación de una API REST con SpringBoot e Hibernate:
Es un sistema arquitectónico para diseñar sistemas distribuidos que se basa en estándares y protocolos web existentes.  
La idea es que estas operaciones CRUD como leer se realizen utilizando métodos HTTP estándar.
```
Por normá general:
Para Guardar: api/proveedores [POST]
Para Eliminar: api/proveedores/1 [DELETE]
Para Modificar y Actualizar: api/proveedores/1 [PUT] 
Para traer 1: api/proveedores/1 [GET]
Para traer todos: api/proveedores [GET]
```
