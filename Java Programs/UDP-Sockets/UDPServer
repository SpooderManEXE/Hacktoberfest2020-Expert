import java.net.*;
import java.util.Scanner;
// Java Socket Connections - Server
public class UdpServer {
    public static void main(String args[]) throws Exception {
        DatagramSocket ds = new DatagramSocket(9875);
        Scanner in = new Scanner(System.in);
        while (true) {
            //	Receive
            byte[] inByte = new byte[1024];
            DatagramPacket dpReceive = new DatagramPacket(inByte, inByte.length);
            ds.receive(dpReceive);
            String inStr = new String(dpReceive.getData());
            System.out.println(inStr);

            // Send
            String outStr = in.nextLine();
            byte[] outByte = outStr.getBytes();
            InetAddress address = dpReceive.getAddress();
            int port = dpReceive.getPort();
            DatagramPacket dpSend = new DatagramPacket(outByte, outByte.length, address, port);
            ds.send(dpSend);

            in.close();
        }
    }
}
