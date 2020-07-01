package com.company;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class TestMain {

    //private Calculadora calc;

    @Before
    public void init(){
        //calc = new Calculadora();
    }

    @Test
    public void inicializarCalculadora(){
        Calculadora cal = new Calculadora();
        Assert.assertEquals(0, cal.Valor());
    }

    //Sumar 2+3
    /*@Test
    public void Sumar2_y_3(){
        Calculadora calc = new Calculadora();
        calc.Sumar(2,3);
        Assert.assertEquals(5,calc.Valor());
    }*/


    //Sumar 3+4
    /*@Test
    public void Sumar3_y_4(){
        Calculadora calc = new Calculadora();
        calc.Sumar(3,4);
        Assert.assertEquals(7,calc.Valor());
    }*/

    //Multiplicar
    /*@Test
    public void Multiplicar2_y_4(){
        Calculadora cal = new Calculadora();
        cal.Multiplicar(2,4);
        Assert.assertEquals(8, cal.Valor());
    }*/



}
