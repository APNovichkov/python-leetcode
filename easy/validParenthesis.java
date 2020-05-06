package com.apn.easy;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

public class ValidParanthesis {

    // Time complexity: O(n) -> Only running through the char array once
    // Memory complexity: O(n) -> Because we are storing parenthesis in a stack,
    // which could get as big as the char array.


    public static boolean isValid(String s) {
        char[] charArr = s.toCharArray();
        int stringLength = s.toCharArray().length;
        HashMap<Character, Character> hm = new HashMap<>();
        hm.put(')', '(');
        hm.put('}', '{');
        hm.put(']', '[');

        System.out.println("String length: " + stringLength);
        if(stringLength%2 != 0) return false;

        Stack<Character> stack = new Stack<>();

        for(char ch: s.toCharArray()){

            if(stack.size() == 0 && !hm.containsValue(ch)) return false;
//            if(stack.size() >= s.length()-1 && !hm.containsKey(ch)) return false;

            if (hm.containsKey(ch)) {
                char sChar = stack.pop();
                System.out.println("Popping " + sChar + " from stack");
                System.out.println("Comparing: " + sChar + " to: " + hm.get(ch));
                if (sChar != hm.get(ch)) return false;
            } else {
                System.out.println("Pushing " + ch + " to stack");
                stack.push(ch);
            }
        }

        if (stack.size() != 0) {
            return false;
        }

        return true;
    }
}
