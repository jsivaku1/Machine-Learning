import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayesSimple;
import weka.classifiers.trees.J48;
import weka.core.Instances;
import java.util.Random;


public class ModelSelection {
        public static void main(String[] args) throws Exception { 
                BufferedReader datafile = readDataFile("train.arff"); 
                Instances data = new Instances(datafile); 
                data.setClassIndex(0); 
  
//J48 for unpruned tree on training with 10-fold Cross Validation                
                  J48 myTree = new J48();
                   myTree.setUnpruned(true);                  
                   Evaluation eval1=new Evaluation(data);
                   eval1.crossValidateModel(myTree, data, 10, new Random(1));
                  double inc_j48_unpruned = eval1.pctIncorrect();
                  System.out.println("Average 10-Fold Cross Validation Error: "+ String.format("%.4f%%", eval1.pctIncorrect()));
                  System.out.println("Classifier:"+myTree.getClass().getSimpleName());
                  System.out.println("Parameters:"+ "\n\t\tunPruned = "+myTree.getUnpruned());                   
                System.out.println("============================================================================");
                 
//J48 for pruned tree with default pruning settings on training with 10-fold Cross Validation                

                 J48 myTree_1 = new J48();
                 Evaluation eval2=new Evaluation(data);
                 String[] options_1 = new String[5];
	            options_1[0] = "-R";
        	   options_1[1] = "-M";
          	 options_1[2] = "2";
          	 options_1[3] = "-N";
         	  options_1[4] = "3";
           	 myTree_1.setOptions(options_1);
                 eval2.crossValidateModel(myTree_1, data, 10, new Random(1));
                 double inc_j48_pruned_1 = eval2.pctIncorrect();
                 System.out.println("Average 10-Fold Cross Validation Error: "+ String.format("%.4f%%", eval2.pctIncorrect()));              
                 System.out.println("Classifier:"+myTree_1.getClass().getSimpleName());
                  System.out.println("Parameters:"+ "\n\t\tReducedErrorPruning = "+myTree_1.getReducedErrorPruning() + "\n\t\tMinNumObj = " +myTree_1.getMinNumObj() +"\n\t\tNumFolds ="+myTree_1.getNumFolds());
                  System.out.println("============================================================================");
                
                 
                 
//J48 for pruned tree  on best parameter settings for training with 10-fold Cross Validation                
   
                 J48 myTree_2 = new J48();
                 Evaluation eval3=new Evaluation(data);
                 String[] options_2 = new String[5];
           	 options_2[0] = "-R";
          	 options_2[1] = "-M";
          	 options_2[2] = "1";
          	 options_2[3] = "-N";
          	 options_2[4] = "4";
           	 myTree_2.setOptions(options_2);
                 eval3.crossValidateModel(myTree_2, data, 10, new Random(1));
                 double inc_j48_pruned_2 = eval3.pctIncorrect();
                 System.out.println("Average 10-Fold Cross Validation Error: "+ String.format("%.4f%%", eval3.pctIncorrect()));
                  System.out.println("Classifier:"+myTree_2.getClass().getSimpleName());
                  System.out.println("Parameters:"+ "\n\t\tReducedErrorPruning = "+myTree_2.getReducedErrorPruning() + "\n\t\tMinNumObj = " +myTree_2.getMinNumObj() +"\n\t\tNumFolds ="+myTree_2.getNumFolds());
                System.out.println("============================================================================");
                
                 
                 
                 
//NaiveBayesSimple for pruned tree on training with 10-fold Cross Validation                 
                  NaiveBayesSimple nbs = new NaiveBayesSimple();
                  Evaluation evalnbs = new Evaluation(data);
                  evalnbs.crossValidateModel(nbs, data, 10, new Random(1));
                  double inc_nbs_cv = evalnbs.pctIncorrect();
                  System.out.println("\nAverage 10-Fold Cross Validation Error: "+ String.format("%.4f%%",evalnbs.pctIncorrect()));
                  System.out.println("Classifier:"+nbs.getClass().getSimpleName());
                    System.out.println("\n============================================================================");
                   
                  
//Selecting based classifier based on the error estimate                  
                  Classifier bestClassifier = null;
                  
                  if(inc_j48_unpruned < inc_j48_pruned_1 && inc_j48_unpruned < inc_j48_pruned_2 &&  inc_j48_unpruned<inc_nbs_cv)
                      bestClassifier = myTree;
                  else if(inc_j48_pruned_1 < inc_j48_unpruned && inc_j48_pruned_1 < inc_j48_pruned_2 &&  inc_j48_pruned_1<inc_nbs_cv)
                      bestClassifier = myTree_1;   
                  else if(inc_j48_pruned_2 < inc_j48_unpruned && inc_j48_pruned_2 < inc_j48_pruned_1 &&  inc_j48_pruned_2<inc_nbs_cv)
                     bestClassifier = myTree_2;
                  else if(inc_nbs_cv < inc_j48_unpruned && inc_nbs_cv < inc_j48_pruned_1 &&  inc_nbs_cv<inc_j48_pruned_2)
                      bestClassifier = nbs;
                  
                  System.out.println("Evaluation on Test set using best classifer");
                  System.out.println("- - - - - - - - - - - - - - - - - - - - - - ");
                  System.out.println("Best classifier selected:" + bestClassifier.getClass().getSimpleName());
                  
//Evaluating the model on test data using the best parameters
                 BufferedReader traindata = readDataFile("train.arff"); 
                 BufferedReader testdata = readDataFile("test.arff"); 
                Instances train = new Instances(traindata);
          	  train.setClassIndex(0);
           	 Instances test = new Instances(testdata);
                 test.setClassIndex(0);
               
                 bestClassifier.buildClassifier(train); 
                 //eval classifier after test
                 Evaluation eval = new Evaluation(train); //trainset 
                 eval.evaluateModel(bestClassifier, test); //testset 
                 System.out.println("Incorrectly classified Instances % = "+ String.format("%.4f%%", eval.pctIncorrect()) + "\nMean Absolute Error = " + String.format("%.4f",eval.meanAbsoluteError())+"\n"); 
                  System.out.println("============================================================================");
                 System.out.println("Classification of test set by best classifier");
                 System.out.println(" - - - - - - - - - - - - - - - - - - - - - - ");
                System.out.println(bestClassifier.toString());
                  
        } 
     public static BufferedReader readDataFile(String filename) throws FileNotFoundException { 
                BufferedReader inputReader = null; 
                inputReader = new BufferedReader(new FileReader(filename)); 
                return inputReader; 
        } 
}
