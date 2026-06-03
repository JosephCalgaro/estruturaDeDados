package pkg;

import java.util.ArrayList;

public class Principal {
    public static void main(String[] args){
        ArrayList<String> estacoes = new ArrayList<>();
        estacoes.add("a");
        estacoes.add("b");
        estacoes.add("c");
        estacoes.add("d");
        estacoes.add("e");

        Grafo gAssimetrico = new Grafo(estacoes);
        // a,b
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("a"), gAssimetrico.RetornaIndice("b"));
        // b,c
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("b"), gAssimetrico.RetornaIndice("c"));
        // b,d
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("b"), gAssimetrico.RetornaIndice("d"));
        // c,e
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("c"), gAssimetrico.RetornaIndice("e"));
        // d,a
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("d"), gAssimetrico.RetornaIndice("a"));
        // d,b
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("d"), gAssimetrico.RetornaIndice("b"));
        // d,c
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("d"), gAssimetrico.RetornaIndice("c"));
        // e,d
        gAssimetrico.inserirAresta(gAssimetrico.RetornaIndice("e"), gAssimetrico.RetornaIndice("d"));
        gAssimetrico.mostrarMatriz();
        gAssimetrico.mostrarGrafo();
    }
}
