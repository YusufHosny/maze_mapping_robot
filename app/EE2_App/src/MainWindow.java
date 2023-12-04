import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.concurrent.TimeUnit;

class MainWindow extends JFrame{
    private int currentXSize, currentYSize, currentMineCount;
    private final JPanel centralArea;

    private Icon[] icons;

    private Maze maze;

    private ArrayList<JButton> buttonList;

    MainWindow(String title) {
        super(title);

        // set maze size
        currentXSize = 8;
        currentYSize = 8;

        // get icons
        /*

        ImageIcon[] imageIcons = new ImageIcon[13];

        imageIcons[0] = new ImageIcon("C:\\Users\\Yusuf\\IdeaProjects\\Minesweeper\\icons\\icons\\blank.png");
        imageIcons[9] = new ImageIcon("C:\\Users\\Yusuf\\IdeaProjects\\Minesweeper\\icons\\icons\\mine.png");
        imageIcons[10] = new ImageIcon("C:\\Users\\Yusuf\\IdeaProjects\\Minesweeper\\icons\\icons\\flag.png");
        imageIcons[11] = new ImageIcon("C:\\Users\\Yusuf\\IdeaProjects\\Minesweeper\\icons\\icons\\checked.png");
        imageIcons[12] = new ImageIcon("C:\\Users\\Yusuf\\IdeaProjects\\Minesweeper\\icons\\icons\\caught.png");
        for(int i = 1; i < 9; i++) {
            imageIcons[i] = new ImageIcon("C:\\Users\\Yusuf\\IdeaProjects\\Minesweeper\\icons\\icons\\" + i + ".png");
        }

        icons = new Icon[13];
        for(int i = 0; i < 13; i++) {
            Image img = imageIcons[i].getImage();
            img = img.getScaledInstance(20, 20, Image.SCALE_DEFAULT);
            icons[i] = new ImageIcon(img);
        }

         */





        // initialize the Frame
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(800, 800);

        // create a menu bar and add the selections

        centralArea = new JPanel();
        centralArea.setSize(600, 600);

        JButton mapBtn = new JButton("Begin Mapping");
        centralArea.add(mapBtn);
        mapBtn.addActionListener(e -> this.beginMapping());


        //Adding Components to the frame.
        this.getContentPane().add(BorderLayout.CENTER, centralArea);

        this.setVisible(true);
    }


    public void setButtonIcon(int[] indices, int identifier) {
        JButton button = buttonList.get(indices[0] * currentXSize + indices[1]);
        button.setIcon(icons[identifier]);
    }

    public void beginMapping() {
        generateMazeGUI();
    }

    public void generateMazeGUI() {
        // default board
        maze = new Maze(currentYSize, currentXSize);

        buttonList = new ArrayList<>();
        centralArea.removeAll();

        int[] bounds = { currentYSize, currentXSize };
        JPanel mazePanel = new JPanel(new GridLayout(bounds[0], bounds[1]));

        for(int i = 0; i < bounds[0]; i++){ // y bound
            for(int j = 0; j < bounds[1]; j++){ // x bound
                JButton button = new JButton();
                button.setSize(25, 25);
                buttonList.add(button);
                mazePanel.add(button);
            }
        }
        mazePanel.setVisible(true);
        centralArea.add(BorderLayout.CENTER, mazePanel);
        centralArea.setSize(600, 600);
        refreshContainer(centralArea);
    }

    public void refreshContainer(Container container) {
        container.setVisible(false);
        container.setVisible(true);
    }

}