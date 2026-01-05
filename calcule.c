double calculate_percentage(int correct_answers, int total_questions) {
    return (total_questions > 0) ? (double)correct_answers * 100.0 / total_questions : 0.0;
}