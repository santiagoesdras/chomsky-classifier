# main.py

import streamlit as st
from grammar_parser import parse_grammar
from classifier import classify_grammar
from visualizer import visualize_grammar
from report_generator import generate_report
from automata_analyzer import analyze_automaton

def main():
    st.title("Chomsky Classifier AI")
    
    st.sidebar.header("Input Options")
    input_type = st.sidebar.selectbox("Select Input Type", ["Grammar", "Automaton"])
    
    if input_type == "Grammar":
        grammar_input = st.text_area("Enter Grammar (BNF format):")
        if st.button("Classify Grammar"):
            if grammar_input:
                parsed_grammar = parse_grammar(grammar_input)
                classification, explanation = classify_grammar(parsed_grammar)
                st.write(f"Classification: {classification}")
                st.write(f"Explanation: {explanation}")
                visualize_grammar(parsed_grammar)
                generate_report(parsed_grammar, classification, explanation)
            else:
                st.error("Please enter a valid grammar.")
    
    elif input_type == "Automaton":
        automaton_input = st.text_area("Enter Automaton Definition:")
        if st.button("Classify Automaton"):
            if automaton_input:
                classification, explanation = analyze_automaton(automaton_input)
                st.write(f"Classification: {classification}")
                st.write(f"Explanation: {explanation}")
                visualize_automaton(automaton_input)
                generate_report(automaton_input, classification, explanation)
            else:
                st.error("Please enter a valid automaton definition.")

if __name__ == "__main__":
    main()