import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TemperatureConverter{
    public static void main(String[] args) {
        Controller controller = new Controller();
        controller.start();
    }

    static class Controller {

        private Model model = new Model();
        private View view = new View();

        /**
         * Start the application by showing a window for the user to do something
         */
        public void start() {
            addListener();
        }

        private void addListener() {
            view.sendTemperature(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    Double result = 0.0;
                    Boolean typeOfTemperature = view.getTypeOfTemperature();

                    result = typeOfTemperature ? model.toCelsius(view.getTemperature()) : model.toFahrenheit(view.getTemperature());
                    view.showTemperature(result);
                }
            });

        }
    }

    static class View {

        private JFrame jFrame;
        private JLabel textLabel, response, celsiusText, fahrenheitText;
        private JButton jButton;
        private JTextField jTextField;
        private JRadioButton celsius, fahrenheit;
        private Boolean typeOfTemperature;  //false = Fahrenheit, true = Celsius


        public View() {
            showWindow();
        }

        public void showWindow() {
            jFrame = new JFrame("Temperature Converter");
            Container container = jFrame.getContentPane();
            jFrame.setSize(800, 100);

            jButton = new JButton("Enter");
            jButton.setEnabled(false);

            celsiusText = new JLabel("To Celsius");
            celsius = new JRadioButton();
            celsius.setSelected(false);
            celsius.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    typeOfTemperature = true;
                    jButton.setEnabled(true);
                }
            });

            fahrenheitText = new JLabel("To Fahrenheit");
            fahrenheit = new JRadioButton();
            fahrenheit.setSelected(false);
            fahrenheit.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    typeOfTemperature = false;
                    jButton.setEnabled(true);
                }
            });

            ButtonGroup bgroup = new ButtonGroup();

            bgroup.add(celsius);
            bgroup.add(fahrenheit);

            jTextField = new JTextField("0.0");
            jTextField.setPreferredSize(new Dimension(100, 30));

            textLabel = new JLabel("Enter temperature: ");
            response = new JLabel();

            container.setLayout(new FlowLayout());

            container.add(celsiusText);
            container.add(celsius);

            container.add(fahrenheitText);
            container.add(fahrenheit);

            container.add(textLabel);
            container.add(jTextField);
            container.add(jButton);

            container.add(response);
            jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            jFrame.setVisible(true);
        }

        public void sendTemperature(ActionListener actionListener) {
            jButton.addActionListener(actionListener);
        }

        public Double getTemperature() {
            if (jTextField.getText().trim().length() == 0) {
                return 0.0;
            }
            return Double.parseDouble(jTextField.getText());
        }

        public void showTemperature(Double result) {
            StringBuilder sb = new StringBuilder();
            sb.append(getTemperature() + " degrees in ");

            sb.append(getTypeOfTemperature() ? "Fahrenheit is " + result.toString() + " in Celsius." : "Celsius is " + result.toString() + " in Fahrenheit.");

            response.setText(sb.toString());
        }

        public Boolean getTypeOfTemperature() {
            return typeOfTemperature;
        }
    }

    static class Model {

        public Model() {}

        public Double toCelsius(Double fahrenheit) {
            return Math.round(((fahrenheit- 32) / 1.8000) * 100.0) / 100.0;
        }

        public Double toFahrenheit(Double celsius) {
            return Math.round(((celsius * 1.8) + 32)*100.0)/100.0;
        }
    }
}