import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

import static java.lang.Thread.sleep;


public class GUI implements ActionListener {

    private int x_position=90;
    private int y_position=270;
    private JButton robot;
    private JButton box22;
    private JButton box10;
    private JButton box15;
    private JPanel panel;

    private JFrame frame;
    private ImageIcon robot_image;

    private Timer timer;
    boolean free;

    public GUI() {
        free = true;
        s = Executors.newScheduledThreadPool(1);

        frame = new JFrame();
        panel = new JPanel();

        // Maze Layer 1
        JButton box1 = new JButton();
        //box1.addActionListener(this);
        box1.setBounds(20,20,50,50);
        box1.setBorderPainted(false);
        box1.setBackground(Color.gray);

        JButton box2 = new JButton();
        //box2.addActionListener(this);
        box2.setBounds(80,20,50,50);
        box2.setBorderPainted(false);
        box2.setBackground(Color.gray);

        JButton box3 = new JButton();
        //box3.addActionListener(this);
        box3.setBounds(140,20,50,50);
        box3.setBorderPainted(false);
        box3.setBackground(Color.gray);

        JButton box4 = new JButton();
        //box4.addActionListener(this);
        box4.setBounds(200,20,50,50);
        box4.setBorderPainted(false);
        box4.setBackground(Color.gray);

        JButton box5 = new JButton();
        //box5.addActionListener(this);
        box5.setBounds(260,20,50,50);
        box5.setBorderPainted(false);
        box5.setBackground(Color.gray);

        // Maze Layer 2
        JButton box6 = new JButton();
        //box6.addActionListener(this);
        box6.setBounds(20,80,50,50);
        box6.setBorderPainted(false);
        box6.setBackground(Color.gray);

        JButton box7 = new JButton();
        //box7.addActionListener(this);
        box7.setBounds(80,80,50,50);
        box7.setBorderPainted(false);
        box7.setBackground(Color.gray);

        JButton box8 = new JButton();
        //box8.addActionListener(this);
        box8.setBounds(140,80,50,50);
        box8.setBorderPainted(false);
        box8.setBackground(Color.gray);

        JButton box9 = new JButton();
        //box9.addActionListener(this);
        box9.setBounds(200,80,50,50);
        box9.setBorderPainted(false);
        box9.setBackground(Color.gray);

        box10 = new JButton();
        //box10.addActionListener(this);
        box10.setBounds(260,80,50,50);
        box10.setBorderPainted(false);
        box10.setBackground(Color.gray);

        // Maze Layer 3
        JButton box11 = new JButton();
        //box11.addActionListener(this);
        box11.setBounds(20,140,50,50);
        box11.setBorderPainted(false);
        box11.setBackground(Color.gray);

        JButton box12 = new JButton();
        //box12.addActionListener(this);
        box12.setBounds(80,140,50,50);
        box12.setBorderPainted(false);
        box12.setBackground(Color.gray);

        JButton box13 = new JButton();
        //box13.addActionListener(this);
        box13.setBounds(140,140,50,50);
        box13.setBorderPainted(false);
        box13.setBackground(Color.gray);

        JButton box14 = new JButton();
        //box14.addActionListener(this);
        box14.setBounds(200,140,50,50);
        box14.setBorderPainted(false);
        box14.setBackground(Color.gray);

        box15 = new JButton();
        //box15.addActionListener(this);
        box15.setBounds(260,140,50,50);
        box15.setBorderPainted(false);
        box15.setBackground(Color.gray);

        // Maze Layer 4
        JButton box16 = new JButton();
        //box16.addActionListener(this);
        box16.setBounds(20,200,50,50);
        box16.setBorderPainted(false);
        box16.setBackground(Color.gray);

        JButton box17 = new JButton();
        //box17.addActionListener(this);
        box17.setBounds(80,200,50,50);
        box17.setBorderPainted(false);
        box17.setBackground(Color.gray);

        JButton box18 = new JButton();
        //box18.addActionListener(this);
        box18.setBounds(140,200,50,50);
        box18.setBorderPainted(false);
        box18.setBackground(Color.gray);

        JButton box19 = new JButton();
        //box19.addActionListener(this);
        box19.setBounds(200,200,50,50);
        box19.setBorderPainted(false);
        box19.setBackground(Color.gray);

        JButton box20 = new JButton();
        //box20.addActionListener(this);
        box20.setBounds(260,200,50,50);
        box20.setBorderPainted(false);
        box20.setBackground(Color.gray);

        // Maze Layer 5
        JButton box21 = new JButton();
        //box21.addActionListener(this);
        box21.setBounds(20,260,50,50);
        box21.setBorderPainted(false);
        box21.setBackground(Color.gray);

        box22 = new JButton();
        //box22.addActionListener(this);
        box22.setBounds(80,260,50,50);
        box22.setBorderPainted(false);
        box22.setBackground(Color.gray);

        JButton box23 = new JButton();
        //box23.addActionListener(this);
        box23.setBounds(140,260,50,50);
        box23.setBorderPainted(false);
        box23.setBackground(Color.gray);

        JButton box24 = new JButton();
        //box24.addActionListener(this);
        box24.setBounds(200,260,50,50);
        box24.setBorderPainted(false);
        box24.setBackground(Color.gray);

        JButton box25 = new JButton();
        //box25.addActionListener(this);
        box25.setBounds(260,260,50,50);
        box25.setBorderPainted(false);
        box25.setBackground(Color.gray);

        //squares

        //outside
        JButton sq17 = new JButton();
        sq17.setBounds(10,10,10,10);
        sq17.setBackground(Color.black);
        sq17.setBorderPainted(false);

        JButton sq18 = new JButton();
        sq18.setBounds(70,10,10,10);
        sq18.setBackground(Color.black);
        sq18.setBorderPainted(false);

        JButton sq19 = new JButton();
        sq19.setBounds(130,10,10,10);
        sq19.setBackground(Color.black);
        sq19.setBorderPainted(false);

        JButton sq20 = new JButton();
        sq20.setBounds(190,10,10,10);
        sq20.setBackground(Color.black);
        sq20.setBorderPainted(false);

        JButton sq21 = new JButton();
        sq21.setBounds(250,10,10,10);
        sq21.setBackground(Color.black);
        sq21.setBorderPainted(false);

        JButton sq22 = new JButton();
        sq22.setBounds(310,10,10,10);
        sq22.setBackground(Color.black);
        sq22.setBorderPainted(false);

        JButton sq23 = new JButton();
        sq23.setBounds(10,70,10,10);
        sq23.setBackground(Color.black);
        sq23.setBorderPainted(false);

        JButton sq24 = new JButton();
        sq24.setBounds(10,130,10,10);
        sq24.setBackground(Color.black);
        sq24.setBorderPainted(false);

        JButton sq25 = new JButton();
        sq25.setBounds(10,190,10,10);
        sq25.setBackground(Color.black);
        sq25.setBorderPainted(false);

        JButton sq26 = new JButton();
        sq26.setBounds(10,250,10,10);
        sq26.setBackground(Color.black);
        sq26.setBorderPainted(false);

        JButton sq27 = new JButton();
        sq27.setBounds(10,310,10,10);
        sq27.setBackground(Color.black);
        sq27.setBorderPainted(false);

        JButton sq28 = new JButton();
        sq28.setBounds(70,310,10,10);
        sq28.setBackground(Color.black);
        sq28.setBorderPainted(false);

        JButton sq29 = new JButton();
        sq29.setBounds(130,310,10,10);
        sq29.setBackground(Color.black);
        sq29.setBorderPainted(false);

        JButton sq30 = new JButton();
        sq30.setBounds(190,310,10,10);
        sq30.setBackground(Color.black);
        sq30.setBorderPainted(false);

        JButton sq31 = new JButton();
        sq31.setBounds(250,310,10,10);
        sq31.setBackground(Color.black);
        sq31.setBorderPainted(false);

        JButton sq32 = new JButton();
        sq32.setBounds(310,310,10,10);
        sq32.setBackground(Color.black);
        sq32.setBorderPainted(false);

        JButton sq33 = new JButton();
        sq33.setBounds(310,250,10,10);
        sq33.setBackground(Color.black);
        sq33.setBorderPainted(false);

        JButton sq34 = new JButton();
        sq34.setBounds(310,190,10,10);
        sq34.setBackground(Color.black);
        sq34.setBorderPainted(false);

        JButton sq35 = new JButton();
        sq35.setBounds(310,130,10,10);
        sq35.setBackground(Color.black);
        sq35.setBorderPainted(false);

        JButton sq36 = new JButton();
        sq36.setBounds(310,70,10,10);
        sq36.setBackground(Color.black);
        sq36.setBorderPainted(false);

        //inside
        JButton sq1 = new JButton();
        sq1.setBounds(70,70,10,10);
        sq1.setBackground(Color.black);
        sq1.setBorderPainted(false);

        JButton sq2 = new JButton();
        sq2.setBounds(130,70,10,10);
        sq2.setBackground(Color.black);
        sq2.setBorderPainted(false);

        JButton sq3 = new JButton();
        sq3.setBounds(190,70,10,10);
        sq3.setBackground(Color.black);
        sq3.setBorderPainted(false);

        JButton sq4 = new JButton();
        sq4.setBounds(250,70,10,10);
        sq4.setBackground(Color.black);
        sq4.setBorderPainted(false);

        JButton sq5 = new JButton();
        sq5.setBounds(70,130,10,10);
        sq5.setBackground(Color.black);
        sq5.setBorderPainted(false);

        JButton sq6 = new JButton();
        sq6.setBounds(130,130,10,10);
        sq6.setBackground(Color.black);
        sq6.setBorderPainted(false);

        JButton sq7 = new JButton();
        sq7.setBounds(190,130,10,10);
        sq7.setBackground(Color.black);
        sq7.setBorderPainted(false);

        JButton sq8 = new JButton();
        sq8.setBounds(250,130,10,10);
        sq8.setBackground(Color.black);
        sq8.setBorderPainted(false);

        JButton sq9 = new JButton();
        sq9.setBounds(70,190,10,10);
        sq9.setBackground(Color.black);
        sq9.setBorderPainted(false);

        JButton sq10 = new JButton();
        sq10.setBounds(130,190,10,10);
        sq10.setBackground(Color.black);
        sq10.setBorderPainted(false);

        JButton sq11 = new JButton();
        sq11.setBounds(190,190,10,10);
        sq11.setBackground(Color.black);
        sq11.setBorderPainted(false);

        JButton sq12 = new JButton();
        sq12.setBounds(250,190,10,10);
        sq12.setBackground(Color.black);
        sq12.setBorderPainted(false);

        JButton sq13 = new JButton();
        sq13.setBounds(70,250,10,10);
        sq13.setBackground(Color.black);
        sq13.setBorderPainted(false);

        JButton sq14 = new JButton();
        sq14.setBounds(130,250,10,10);
        sq14.setBackground(Color.black);
        sq14.setBorderPainted(false);

        JButton sq15 = new JButton();
        sq15.setBounds(190,250,10,10);
        sq15.setBackground(Color.black);
        sq15.setBorderPainted(false);

        JButton sq16 = new JButton();
        sq16.setBounds(250,250,10,10);
        sq16.setBackground(Color.black);
        sq16.setBorderPainted(false);


        // top wall
        JButton wall1 = new JButton();
        wall1.setBounds(20,10,50,10);
        wall1.setBackground(Color.black);
        wall1.setBorderPainted(false);

        JButton wall47 = new JButton();
        wall47.setBounds(80,10,50,10);
        wall47.setBackground(Color.black);
        wall47.setBorderPainted(false);

        JButton wall48 = new JButton();
        wall48.setBounds(140,10,50,10);
        wall48.setBackground(Color.black);
        wall48.setBorderPainted(false);

        JButton wall49 = new JButton();
        wall49.setBounds(200,10,50,10);
        wall49.setBackground(Color.black);
        wall49.setBorderPainted(false);

        JButton wall50 = new JButton();
        wall50.setBounds(260,10,50,10);
        wall50.setBackground(Color.black);
        wall50.setBorderPainted(false);

        //left wall
        JButton wall2 = new JButton();
        wall2.setBounds(10,20,10,50);
        wall2.setBackground(Color.black);
        wall2.setBorderPainted(false);

        JButton wall51 = new JButton();
        wall51.setBounds(10,80,10,50);
        wall51.setBackground(Color.black);
        wall51.setBorderPainted(false);

        JButton wall52 = new JButton();
        wall52.setBounds(10,140,10,50);
        wall52.setBackground(Color.black);
        wall52.setBorderPainted(false);

        JButton wall53 = new JButton();
        wall53.setBounds(10,200,10,50);
        wall53.setBackground(Color.black);
        wall53.setBorderPainted(false);

        JButton wall54 = new JButton();
        wall54.setBounds(10,260,10,50);
        wall54.setBackground(Color.black);
        wall54.setBorderPainted(false);

        //bottom wall
        JButton wall3 = new JButton();
        wall3.setBounds(20,310,50,10);
        wall3.setBackground(Color.black);
        wall3.setBorderPainted(false);

        JButton wall55 = new JButton();
        wall55.setBounds(80,310,50,10);
        wall55.setBackground(Color.gray);
        wall55.setBorderPainted(false);

        JButton wall56 = new JButton();
        wall56.setBounds(140,310,50,10);
        wall56.setBackground(Color.black);
        wall56.setBorderPainted(false);

        JButton wall57 = new JButton();
        wall57.setBounds(200,310,50,10);
        wall57.setBackground(Color.black);
        wall57.setBorderPainted(false);

        JButton wall58 = new JButton();
        wall58.setBounds(260,310,50,10);
        wall58.setBackground(Color.black);
        wall58.setBorderPainted(false);

        //right wall
        JButton wall4 = new JButton();
        wall4.setBounds(310,20,10,50);
        wall4.setBackground(Color.black);
        wall4.setBorderPainted(false);

        JButton wall59 = new JButton();
        wall59.setBounds(310,80,10,50);
        wall59.setBackground(Color.gray);
        wall59.setBorderPainted(false);

        JButton wall6 = new JButton();
        wall6.setBounds(310,140,10,50);
        wall6.setBackground(Color.black);
        wall6.setBorderPainted(false);

        JButton wall60 = new JButton();
        wall60.setBounds(310,200,10,50);
        wall60.setBackground(Color.black);
        wall60.setBorderPainted(false);

        JButton wall5 = new JButton();
        wall5.setBounds(310,260,10,50);
        wall5.setBackground(Color.black);
        wall5.setBorderPainted(false);

        //inside walls

        //vertical walls

        //layer 1
        JButton wall24 = new JButton();
        wall24.setBounds(70,20,10,50);
        wall24.setBackground(Color.gray);
        wall24.setBorderPainted(false);

        JButton wall25 = new JButton();
        wall25.setBounds(130,20,10,50);
        wall25.setBackground(Color.gray);
        wall25.setBorderPainted(false);

        JButton wall26 = new JButton();
        wall26.setBounds(190,20,10,50);
        wall26.setBackground(Color.gray);
        wall26.setBorderPainted(false);

        JButton wall27 = new JButton();
        wall27.setBounds(250,20,10,50);
        wall27.setBackground(Color.gray);
        wall27.setBorderPainted(false);

        //layer 2
        JButton wall18 = new JButton();
        wall18.setBounds(70,80,10,50);
        wall18.setBackground(Color.black);
        wall18.setBorderPainted(false);

        JButton wall19 = new JButton();
        wall19.setBounds(130,80,10,50);
        wall19.setBackground(Color.black);
        wall19.setBorderPainted(false);

        JButton wall23 = new JButton();
        wall23.setBounds(190,80,10,50);
        wall23.setBackground(Color.gray);
        wall23.setBorderPainted(false);

        JButton wall28 = new JButton();
        wall28.setBounds(250,80,10,50);
        wall28.setBackground(Color.gray);
        wall28.setBorderPainted(false);

        //layer 3
        JButton wall31 = new JButton();
        wall31.setBounds(70,140,10,50);
        wall31.setBackground(Color.gray);
        wall31.setBorderPainted(false);

        JButton wall30 = new JButton();
        wall30.setBounds(130,140,10,50);
        wall30.setBackground(Color.gray);
        wall30.setBorderPainted(false);

        JButton wall29 = new JButton();
        wall29.setBounds(190,140,10,50);
        wall29.setBackground(Color.gray);
        wall29.setBorderPainted(false);

        JButton wall15 = new JButton();
        wall15.setBounds(250,140,10,50);
        wall15.setBackground(Color.black);
        wall15.setBorderPainted(false);

        //layer 4
        JButton wall9 = new JButton();
        wall9.setBounds(70,200,10,50);
        wall9.setBackground(Color.black);
        wall9.setBorderPainted(false);

        JButton wall10 = new JButton();
        wall10.setBounds(130,200,10,50);
        wall10.setBackground(Color.black);
        wall10.setBorderPainted(false);

        JButton wall12 = new JButton();
        wall12.setBounds(190,200,10,50);
        wall12.setBackground(Color.black);
        wall12.setBorderPainted(false);

        JButton wall32 = new JButton();
        wall32.setBounds(250,200,10,50);
        wall32.setBackground(Color.gray);
        wall32.setBorderPainted(false);

        //layer 5
        JButton wall7 = new JButton();
        wall7.setBounds(70,260,10,50);
        wall7.setBackground(Color.black);
        wall7.setBorderPainted(false);

        JButton wall8 = new JButton();
        wall8.setBounds(130,260,10,50);
        wall8.setBackground(Color.black);
        wall8.setBorderPainted(false);

        JButton wall33 = new JButton();
        wall33.setBounds(190,260,10,50);
        wall33.setBackground(Color.gray);
        wall33.setBorderPainted(false);

        JButton wall34 = new JButton();
        wall34.setBounds(250,260,10,50);
        wall34.setBackground(Color.gray);
        wall34.setBorderPainted(false);



        //horizontal walls

        //layer 1
        JButton wall35 = new JButton();
        wall35.setBounds(20,70,50,10);
        wall35.setBackground(Color.gray);
        wall35.setBorderPainted(false);

        JButton wall17 = new JButton();
        wall17.setBounds(20,130,50,10);
        wall17.setBackground(Color.black);
        wall17.setBorderPainted(false);

        JButton wall36 = new JButton();
        wall36.setBounds(20,190,50,10);
        wall36.setBackground(Color.gray);
        wall36.setBorderPainted(false);

        JButton wall37 = new JButton();
        wall37.setBounds(20,250,50,10);
        wall37.setBackground(Color.gray);
        wall37.setBorderPainted(false);

        //layer 2
        JButton wall38 = new JButton();
        wall38.setBounds(80,70,50,10);
        wall38.setBackground(Color.gray);
        wall38.setBorderPainted(false);

        JButton wall39 = new JButton();
        wall39.setBounds(80,130,50,10);
        wall39.setBackground(Color.gray);
        wall39.setBorderPainted(false);

        JButton wall40 = new JButton();
        wall40.setBounds(80,190,50,10);
        wall40.setBackground(Color.gray);
        wall40.setBorderPainted(false);

        JButton wall41 = new JButton();
        wall41.setBounds(80,250,50,10);
        wall41.setBackground(Color.gray);
        wall41.setBorderPainted(false);

        //layer 3
        JButton wall21 = new JButton();
        wall21.setBounds(140,70,50,10);
        wall21.setBackground(Color.black);
        wall21.setBorderPainted(false);

        JButton wall22 = new JButton();
        wall22.setBounds(140,130,50,10);
        wall22.setBackground(Color.black);
        wall22.setBorderPainted(false);

        JButton wall42 = new JButton();
        wall42.setBounds(140,190,50,10);
        wall42.setBackground(Color.gray);
        wall42.setBorderPainted(false);

        JButton wall43 = new JButton();
        wall43.setBounds(140,250,50,10);
        wall43.setBackground(Color.gray);
        wall43.setBorderPainted(false);

        //layer 4
        JButton wall20 = new JButton();
        wall20.setBounds(200,70,50,10);
        wall20.setBackground(Color.black);
        wall20.setBorderPainted(false);

        JButton wall44 = new JButton();
        wall44.setBounds(200,130,50,10);
        wall44.setBackground(Color.gray);
        wall44.setBorderPainted(false);

        JButton wall11 = new JButton();
        wall11.setBounds(200,190,50,10);
        wall11.setBackground(Color.black);
        wall11.setBorderPainted(false);

        JButton wall13 = new JButton();
        wall13.setBounds(200,250,50,10);
        wall13.setBackground(Color.black);
        wall13.setBorderPainted(false);

        //layer5
        JButton wall16 = new JButton();
        wall16.setBounds(260,70,50,10);
        wall16.setBackground(Color.black);
        wall16.setBorderPainted(false);

        JButton wall45 = new JButton();
        wall45.setBounds(260,130,50,10);
        wall45.setBackground(Color.gray);
        wall45.setBorderPainted(false);

        JButton wall46 = new JButton();
        wall46.setBounds(260,190,50,10);
        wall46.setBackground(Color.gray);
        wall46.setBorderPainted(false);

        JButton wall14 = new JButton();
        wall14.setBounds(260,250,50,10);
        wall14.setBackground(Color.black);
        wall14.setBorderPainted(false);


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

        robot = new JButton();
        robot.setBounds(x_position,y_position,30,30);
        robot.setBorderPainted(false);
        robot.setBackground(Color.yellow);

        //robot_image = new ImageIcon("robot.jfif");
        //box22.setIcon(robot_image);



        // panel settings
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        panel.setLayout(null);
        panel.setBackground(Color.magenta);

        panel.add(button1);
        panel.add(button2);
        panel.add(maze_label);
        panel.add(robot);


        panel.add(box1);
        panel.add(box2);
        panel.add(box3);
        panel.add(box4);
        panel.add(box5);
        panel.add(box6);
        panel.add(box7);
        panel.add(box8);
        panel.add(box9);
        panel.add(box10);
        panel.add(box11);
        panel.add(box12);
        panel.add(box13);
        panel.add(box14);
        panel.add(box15);
        panel.add(box16);
        panel.add(box17);
        panel.add(box18);
        panel.add(box19);
        panel.add(box20);
        panel.add(box21);
        panel.add(box22);
        panel.add(box23);
        panel.add(box24);
        panel.add(box25);

        panel.add(wall1);
        panel.add(wall2);
        panel.add(wall3);
        panel.add(wall4);
        panel.add(wall5);
        panel.add(wall6);
        panel.add(wall7);
        panel.add(wall8);
        panel.add(wall9);
        panel.add(wall10);
        panel.add(wall11);
        panel.add(wall12);
        panel.add(wall13);
        panel.add(wall14);
        panel.add(wall15);
        panel.add(wall16);
        panel.add(wall17);
        panel.add(wall18);
        panel.add(wall19);
        panel.add(wall20);
        panel.add(wall21);
        panel.add(wall22);
        panel.add(wall23);
        panel.add(wall24);
        panel.add(wall25);
        panel.add(wall26);
        panel.add(wall27);
        panel.add(wall28);
        panel.add(wall29);
        panel.add(wall30);
        panel.add(wall31);
        panel.add(wall32);
        panel.add(wall33);
        panel.add(wall34);
        panel.add(wall35);
        panel.add(wall36);
        panel.add(wall37);
        panel.add(wall38);
        panel.add(wall39);
        panel.add(wall40);
        panel.add(wall41);
        panel.add(wall42);
        panel.add(wall43);
        panel.add(wall44);
        panel.add(wall45);
        panel.add(wall46);
        panel.add(wall47);
        panel.add(wall48);
        panel.add(wall49);
        panel.add(wall50);
        panel.add(wall51);
        panel.add(wall52);
        panel.add(wall53);
        panel.add(wall54);
        panel.add(wall55);
        panel.add(wall56);
        panel.add(wall57);
        panel.add(wall58);
        panel.add(wall59);
        panel.add(wall60);

        panel.add(sq1);
        panel.add(sq2);
        panel.add(sq3);
        panel.add(sq4);
        panel.add(sq5);
        panel.add(sq6);
        panel.add(sq7);
        panel.add(sq8);
        panel.add(sq9);
        panel.add(sq10);
        panel.add(sq11);
        panel.add(sq12);
        panel.add(sq13);
        panel.add(sq14);
        panel.add(sq15);
        panel.add(sq16);
        panel.add(sq17);
        panel.add(sq18);
        panel.add(sq19);
        panel.add(sq20);
        panel.add(sq21);
        panel.add(sq22);
        panel.add(sq23);
        panel.add(sq24);
        panel.add(sq25);
        panel.add(sq26);
        panel.add(sq27);
        panel.add(sq28);
        panel.add(sq29);
        panel.add(sq30);
        panel.add(sq31);
        panel.add(sq32);
        panel.add(sq33);
        panel.add(sq34);
        panel.add(sq35);
        panel.add(sq36);



        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Project App");
        frame.setSize(1000, 700);
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);


    }

    public static void main(String[] args) {
        new GUI();
    }


    @Override
    public void actionPerformed(ActionEvent e) {
        moveHorizontal(70);
        moveVertical(-70);

    }


    ScheduledExecutorService s;
    //to change between mazes
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
                x_position += delta;
                robot.setBounds(x_position,y_position,30,30);
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
                y_position += delta;
                robot.setBounds(x_position, y_position, 30, 30);
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
