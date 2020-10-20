package JavaLab5;

import java.net.*;
import java.util.Scanner;
// Java Socket Connections - Client
public class UdpClient {
        public static void main(String args[]) throws Exception {
        DatagramSocket ds = new DatagramSocket();
        Scanner in = new Scanner(System.in);

        //		Send
        String outStr = in.nextLine();
        byte[] outByte = outStr.getBytes();
        InetAddress address = InetAddress.getLocalHost();
        int port = 9875;
        DatagramPacket dpSend = new DatagramPacket(outByte, outByte.length, address, port);
            ds.send(dpSend);

        //Receive
        byte[] inByte = new byte[1024];
        DatagramPacket dpReceive = new DatagramPacket(inByte, inByte.length);
            ds.receive(dpReceive);
        String inStr = new String(dpReceive.getData());
            System.out.println(inStr);

            in.close();
            ds.close();
}
}
