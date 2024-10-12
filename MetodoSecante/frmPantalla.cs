using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MetodoSecante
{
    public partial class frmPantalla : Form
    {
        public frmPantalla()
        {
            InitializeComponent();
        }

        private void frmPantalla_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void lblFuncion_Click(object sender, EventArgs e)
        {

        }

        private void btnCalcular_Click(object sender, EventArgs e)
        {

            try
            {
                // Parsear entradas desde los TextBox
                double x0 = double.Parse(txtX0.Text);
                double x1 = double.Parse(txtX1.Text);
                double tolerancia = double.Parse(txtTolerancia.Text);
                int maxIteraciones = int.Parse(txtIteraciones.Text);

                // Definir función
                Func<double, double> funcion = EvaluarFuncion(txtFuncion.Text);

                // Aplicar el método de la secante
                double resultado = MetodoSecante(funcion, x0, x1, tolerancia, maxIteraciones);

                // Mostrar resultado
                txtResultado.Text = resultado.ToString();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Ocurrió un error: " + ex.Message);
            }



        }





        private double MetodoSecante(Func<double, double> f, double x0, double x1, double tolerancia, int maxIteraciones)
        {
            double xPrevio = x0;
            double xActual = x1;
            double xSiguiente;

            for (int i = 0; i < maxIteraciones; i++)
            {
                double fXPrevio = f(xPrevio);
                double fXActual = f(xActual);

                // Comprobar si la diferencia es menor que la tolerancia
                if (Math.Abs(fXActual) < tolerancia)
                {
                    return xActual;
                }

                // Fórmula del método de la secante
                xSiguiente = xActual - fXActual * (xActual - xPrevio) / (fXActual - fXPrevio);

                // Comprobar si la diferencia entre iteraciones es menor que la tolerancia
                if (Math.Abs(xSiguiente - xActual) < tolerancia)
                {
                    return xSiguiente;
                }

                // Actualizar variables para la siguiente iteración
                xPrevio = xActual;
                xActual = xSiguiente;
            }

            throw new Exception("No se encontró la raíz en el número máximo de iteraciones");
        }

        private Func<double, double> EvaluarFuncion(string funcion)
        {
            // Aquí podrías usar una librería como NCalc o escribir un parser simple para la función.
            // Por ahora, vamos a devolver una función fija como ejemplo (modifícalo según tus necesidades).

            // Ejemplo: Si la función es "x^2 - 2"
            return x => Math.Pow(x, 2) - 2;
        }

        private void btnLimpiar_Click(object sender, EventArgs e)
        {
            txtFuncion.Text = "";
            txtX0.Text = "";
            txtX1.Text = "";
            txtTolerancia.Text = "";
            txtIteraciones.Text = "";
            txtResultado.Text = "";


        }
    }
}
