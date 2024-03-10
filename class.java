public class Main {
    public static void main(String[] args) {
        // Exemple d'utilisation de la classe Personne
        Personne personne = new Personne("Doe", "John", 30);

        // Affichage des informations
        System.out.println("Nom : " + personne.Nom);
        System.out.println("Prenom : " + personne.Prenom);
        System.out.println("Age : " + personne.Age);
    }

    public static class Personne {
        protected String Nom;
        protected String Prenom;
        protected int Age;

        public Personne(String n, String p, int a) {
            Nom = n;
            Prenom = p;
            Age = a;
        }
    }
}
