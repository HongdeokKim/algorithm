package Q2;

import java.util.*;

class UserSolution {
    private static HashMap<String, HashMap<Integer, ArrayList<Integer>>> database;

    private static int ite = 0;

    public void init() {
        database = new HashMap<String, HashMap<Integer, ArrayList<Integer>>>();

        ite = ite + 1;

        return;
    }

    public int add(int mId, int mGrade, char mGender[], int mScore) {

        String ggKey = Integer.toString(mGrade) + new String(mGender);

        // if(ite == 20) {
        //     System.out.println("add : " + ggKey + ", " + mGrade + ", "  + mScore + ", " + mId);
        // }
        
        if(!database.containsKey(ggKey)) { // 테이블 없으면 해시맵 만들어줌
            database.put(ggKey, new HashMap<Integer, ArrayList<Integer>>());
        }

        // 이제는 무조건 있음
        HashMap<Integer, ArrayList<Integer>> scoreBoard = database.get(ggKey);
        if(!scoreBoard.containsKey(mScore)) { // 값이 없으면 만들어줌
            scoreBoard.put(mScore, new ArrayList<Integer>());
        }
        ArrayList<Integer> idBoard = scoreBoard.get(mScore); // id를 추가
        idBoard.add(mId);

        // 반환 값 계산 - 가장 score가 크고 id도 가장 큰
        int maxScore = Collections.max(scoreBoard.keySet());
        int max = Collections.max(scoreBoard.get(maxScore));
        if(ite == 20) {
            System.out.println(max);
        }
        return max;
    }

    public int remove(int mId) {
        String ggKey_s = null;

        for(String ggKey : database.keySet()) {
            HashMap<Integer, ArrayList<Integer>> scoreBoard = database.get(ggKey);

            for(Integer score : scoreBoard.keySet()) {
                ArrayList<Integer> idBoard = scoreBoard.get(score);
                
                if(idBoard.contains(mId)) { // 해당 id가 있으면 
                    idBoard.remove((Object)mId); // 삭제
                    
                    if(idBoard.isEmpty()) { // 해당 점수에 존재하는 id가 없으면 -> mem
                        scoreBoard.remove(score); // 스코어보드 삭제
                    }
                    ggKey_s = ggKey;
                    if(ite == 20) {
                        System.out.println("remove : " + ggKey + ", " + score + ", " + mId);
                    }
                    
                    break;
                }
            }
        }

        if(ggKey_s == null) {
            if(ite == 20) {
                System.out.println("remove : cannot find");
            }
            return 0;
        }

        HashMap<Integer, ArrayList<Integer>> scoreBoard = database.get(ggKey_s);
        if(scoreBoard.keySet().isEmpty()) {
            return 0;
        }
        int minScore = Collections.min(scoreBoard.keySet());
        int min = Collections.min(scoreBoard.get(minScore));
        if(ite == 20) {
            System.out.println(min);
        }
        return min;
    }

    public int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][], int mScore) {

        if(ite == 20) {
            System.out.println("query : " + mGradeCnt + ", " + mGenderCnt + ", " + mScore);
        }
        int score = 300000;
        
        HashMap<Integer, ArrayList<Integer>> queryBoard = new HashMap<Integer, ArrayList<Integer>>();

        for(int i = 0; i < mGradeCnt; i++) {
            for(int j = 0; j < mGenderCnt; j++) {
                String ggKey = Integer.toString(mGrade[i]) + new String(mGender[j]);
                
                if(database.containsKey(ggKey)) {
                    HashMap<Integer, ArrayList<Integer>> scoreBoard = database.get(ggKey);
                    if(scoreBoard.keySet().isEmpty()) {
                        System.out.println(ggKey + "is empty");
                        continue;
                    }
                    for(Integer sc : scoreBoard.keySet()) {
                        int comp = sc - mScore;

                        if(0 <= comp && comp <= score) {
                            score = comp;
                            if(ite == 20) {
                                System.out.println("query++ : " + ggKey + " " + comp + ", " + sc + ", " +mScore);
                            }
                            ArrayList<Integer> ids = scoreBoard.get(sc);
                            if(queryBoard.containsKey(sc)) {
                                System.out.println("값겹침");
                                queryBoard.get(sc).addAll(ids);
                            }
                            else {
                                queryBoard.put(sc, ids);
                            }
                        }
                        else {
                            continue;
                        }
                    }
                }

            }
        }

        if(queryBoard.keySet().isEmpty()) {
            return 0;
        }
        int minScore = Collections.min(queryBoard.keySet());
        System.out.println(minScore);
        int min = Collections.min(queryBoard.get(minScore));
        if(ite == 20) {
            System.out.println(min);
        }
        
        return min;
    }
}

