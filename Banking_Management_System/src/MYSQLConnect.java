/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author IamJRKOO6
 */
import java.util.*;
import java.sql.*;
import javax.swing.*;
public class MYSQLConnect {
    Connection conn=null;
    public static Connection JK(String host,String port,String database,String username,String password){
        String url="jdbc:mysql://"+host+":"+port+"/"+database;
        try{
            Class.forName("com.mysql.jdbc.Driver");
            Connection conn=DriverManager.getConnection(url,username,password);
            return conn;
        }catch(Exception e){
            JOptionPane.showMessageDialog(null,e);
            return null;
        }
    }
}
