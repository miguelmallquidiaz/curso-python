package atl.academy.coursemanager.models;

import jakarta.persistence.*;
import lombok.Data;

@Data //anotación para automatizar
@Entity //como sera mapeada la base de datos
@Table(name = "STUDENT")//Mapadeada en una tabla
public class Student {
    @Id//pk
    @GeneratedValue(strategy = GenerationType.IDENTITY)//incrementa automaticamente el pk
    @Column(name = "IdStudent")
    private Long id;

    @Column(name = "NameStudent")
    private String nameStudent;

    //La columna debe tener un valor unico y no un valor vacío.
    @Column(name = "Email", unique = true, nullable = false)
    private String email;

    @Column(name = "Phone", unique = true, nullable = false)
    private String phone;
}