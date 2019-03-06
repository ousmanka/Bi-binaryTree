package project;

import java.util.ArrayList;
import java.util.Collections;

public class redTeam extends InterfaceClass {

	String input;

	@Override
	public int score(int score) {
		if(isRight() == true) {
			score++;
		}
		return score;
	}

	@Override
	public String guessedWord(ArrayList<String> input) {
		return Collections.max(input);
	}
	
	public boolean isRight() {
		blueTeam one = new blueTeam();
		ArrayList<String> words = new ArrayList<>();
		if(input == one.guessedWord(words)) {
			return true;
			
		}
		return false;
	}

}
