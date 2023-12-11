import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;


import static java.lang.Thread.sleep;

public class GUI_2 implements ActionListener{
    private int robot_x_position = 90;
    private int robot_y_position = 330;
    private JButton robot;
    private JButton box22;
    private JButton box10;
    private JButton box15;
    private JPanel panel;

    private JFrame frame;
    private ImageIcon robot_image;
    private Timer timer;
    boolean free;

    private int box_x_position = 20;
    private int box_y_position = 20;
    private int sq_x_position = 10;
    private int sq_y_position = 10;
    private int wall_x_position_ver = 10;
    private int wall_y_position_ver = 20;
    private int wall_x_position_hor = 20;
    private int wall_y_position_hor = 10;
    private JButton up;
    private JButton down;
    private JButton left;
    private JButton right;


    ScheduledExecutorService s;

    public GUI_2() {
        free = true;
        s = Executors.newScheduledThreadPool(1);

        frame = new JFrame();
        panel = new JPanel();

        robot_image = new ImageIcon("robot.jfif");

        Image img = robot_image.getImage();
        Image new_image = img.getScaledInstance(30,30, Image.SCALE_SMOOTH);
        robot_image = new ImageIcon(new_image);

        robot = new JButton();
        robot.setBounds(robot_x_position,robot_y_position,30,30);
        robot.setBorderPainted(false);
        robot.setIcon(robot_image);
        panel.add(robot);

        //boxes
        List<JButton> boxlist = new ArrayList<JButton>();
        int x_dir=0;
        int y_dir=0;
        for (int i=0; i<25; i++)
        {
            x_dir+=60;
            if (i%5 == 0) {
                y_dir+=60;
                x_dir = 0;
            }
            JButton box = new JButton();
            box.setBounds(box_x_position+x_dir, box_y_position+y_dir,50,50);
            box.setBorderPainted(false);
            box.setBackground(Color.gray);
            boxlist.add(box);
            panel.add(box);
        }

        //squares as corners
        List<JButton> squarelist = new ArrayList<JButton>();
        int x_sq=0;
        int y_sq=0;
        for (int j=0; j<36; j++)
        {
            x_sq+=60;
            if (j%6 == 0) {
                y_sq+=60;
                x_sq=0;
            }
            JButton sq = new JButton();
            sq.setBounds(sq_x_position+x_sq,sq_y_position+y_sq,10,10);
            sq.setBackground(Color.black);
            sq.setBorderPainted(false);
            squarelist.add(sq);
            panel.add(sq);
        }

        //walls

        //vertical walls
        List<JButton> walllist_ver = new ArrayList<JButton>();
        int x_wall_ver=0;
        int y_wall_ver=0;
        for (int a=0; a<30; a++)
        {
            x_wall_ver+=60;
            if (a%6 == 0) {
                y_wall_ver+=60;
                x_wall_ver=0;
            }
            JButton wall = new JButton();
            wall.setBounds(wall_x_position_ver+x_wall_ver,wall_y_position_ver+y_wall_ver,10,50);
            wall.setBackground(Color.black);
            wall.setBorderPainted(false);
            walllist_ver.add(wall);
            panel.add(wall);
        }

        //horizontal walls
        List<JButton> walllist_hor = new ArrayList<JButton>();
        int x_wall_hor=0;
        int y_wall_hor=0;
        for (int a=0; a<30; a++) {
            x_wall_hor += 60;
            if (a % 5 == 0) {
                y_wall_hor += 60;
                x_wall_hor = 0;
            }
            JButton wall = new JButton();
            wall.setBounds(wall_x_position_hor + x_wall_hor, wall_y_position_hor + y_wall_hor, 50, 10);
            wall.setBackground(Color.black);
            wall.setBorderPainted(false);
            walllist_hor.add(wall);
            panel.add(wall);
        }

        //inner walls settings
        walllist_ver.get(1).setBackground(Color.gray);
        walllist_ver.get(2).setBackground(Color.gray);
        walllist_ver.get(3).setBackground(Color.gray);
        walllist_ver.get(4).setBackground(Color.gray);
        walllist_ver.get(9).setBackground(Color.gray);
        walllist_ver.get(10).setBackground(Color.gray);
        walllist_ver.get(11).setBackground(Color.gray);
        walllist_ver.get(13).setBackground(Color.gray);
        walllist_ver.get(14).setBackground(Color.gray);
        walllist_ver.get(15).setBackground(Color.gray);
        walllist_ver.get(22).setBackground(Color.gray);
        walllist_ver.get(27).setBackground(Color.gray);
        walllist_ver.get(28).setBackground(Color.gray);

        walllist_hor.get(5).setBackground(Color.gray);
        walllist_hor.get(6).setBackground(Color.gray);
        walllist_hor.get(11).setBackground(Color.gray);
        walllist_hor.get(13).setBackground(Color.gray);
        walllist_hor.get(14).setBackground(Color.gray);
        walllist_hor.get(15).setBackground(Color.gray);
        walllist_hor.get(16).setBackground(Color.gray);
        walllist_hor.get(17).setBackground(Color.gray);
        walllist_hor.get(19).setBackground(Color.gray);
        walllist_hor.get(20).setBackground(Color.gray);
        walllist_hor.get(21).setBackground(Color.gray);
        walllist_hor.get(22).setBackground(Color.gray);
        walllist_hor.get(26).setBackground(Color.gray);

        /*
        int x_node = 0;
        int y_node  0;
        for (int n=0; n<25; n++)
        {
            x_node += 50;

        }

         */


        //buttons
        JButton button1 = new JButton("Start");
        button1.addActionListener(this);
        button1.setBackground(Color.green);
        button1.setBounds(400, 220, 70,40);
        button1.setFocusable(false);

        String[] maze_types = {"type 1", "type 2", "type3"};
        JComboBox button2 = new JComboBox(maze_types);
        button2.setSelectedIndex(0);
        //button2.addActionListener(this);
        button2.setBackground(Color.green);
        button2.setBounds(400, 150, 100,40);
        button2.setFocusable(false);

        JLabel maze_label = new JLabel("Select Maze:");
        maze_label.setBounds(400,120,100,30);


        //moving buttons
        up = new JButton();
        up.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                robot_y_position-=10;
                robot.setBounds(robot_x_position, robot_y_position,30,30);
                panel.repaint();
            }
        });
        up.setBackground(Color.orange);
        up.setBorderPainted(false);
        up.setFocusable(false);
        up.setBounds(500, 250,0,0);
        up.setMnemonic(KeyEvent.VK_UP);
        panel.add(up);

        down = new JButton();
        down.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                robot_y_position+=10;
                robot.setBounds(robot_x_position, robot_y_position,30,30);
                panel.repaint();
            }
        });
        down.setBackground(Color.orange);
        down.setBorderPainted(false);
        down.setFocusable(false);
        down.setBounds(500, 300,0,0);
        down.setMnemonic(KeyEvent.VK_DOWN);
        panel.add(down);

        left = new JButton();
        left.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                robot_x_position-=10;
                robot.setBounds(robot_x_position, robot_y_position,30,30);
                panel.repaint();
            }
        });
        left.setBackground(Color.orange);
        left.setBorderPainted(false);
        left.setFocusable(false);
        left.setBounds(450, 300,0,0);
        left.setMnemonic(KeyEvent.VK_LEFT);
        panel.add(left);

        right = new JButton();
        right.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                robot_x_position+=10;
                robot.setBounds(robot_x_position, robot_y_position,30,30);
                panel.repaint();
            }
        });
        right.setBackground(Color.orange);
        right.setBorderPainted(false);
        right.setFocusable(false);
        right.setBounds(550, 300,0,0);
        right.setMnemonic(KeyEvent.VK_RIGHT);
        panel.add(right);



        //robot_image = new ImageIcon("robot.jfif");
        //boxlist.get(21).setIcon(robot_image);

        // panel settings
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        panel.setLayout(null);
        panel.setBackground(Color.orange);

        panel.add(button1);
        panel.add(button2);
        panel.add(maze_label);

        //frame settings
        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Project App");
        frame.setSize(1000, 700);
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);

    }

    public static void main(String[] args) {
        new GUI_2();
    }


    public void actionPerformed(ActionEvent e) {

    }


    public void moveHorizontal(int distance) {
        int delta;
        if (distance < 0) {
            delta = -1;
            distance = -distance;
        }
        else {
            delta = 1;
        }

        //while(!free) {}
        //free = false;
        for (int i=0; i<distance; i++)
        {
            s.schedule(() -> {
                robot_x_position += delta;
                robot.setBounds(robot_x_position,robot_y_position,30,30);
                panel.repaint();
            }, 50*i, TimeUnit.MILLISECONDS );


        }
        s.schedule(() -> free = true, 50*distance, TimeUnit.MILLISECONDS);
    }

    public void moveVertical(int distance) {
        int delta;
        if (distance < 0) {
            delta = -1;
            distance = -distance;
        }
        else {
            delta = 1;
        }

        //while(!free) {}
        //free = false;
        for (int i=0; i<distance; i++)
        {
            s.schedule(() -> {
                robot_y_position += delta;
                robot.setBounds(robot_x_position, robot_y_position, 30, 30);
                panel.repaint();

            }, 50*i, TimeUnit.MILLISECONDS );

        }
        s.schedule(() -> free = true, 50*distance, TimeUnit.MILLISECONDS);

    }



    public void changeMaze() {

    }


    public void wait(int milliseconds)
    {
        try
        {
            sleep(milliseconds);
        }
        catch (Exception e)
        {
            // ignoring exception at the moment
        }
    }
}


