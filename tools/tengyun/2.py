import pandas as pd
from gensim.matutils import cossim
import ergin

def compare_similarity_and_score(excel_file):
    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file)

    # Add new columns (D, E, and F) to store similarity results, marks, and scores
    df['Similarity Score'] = None
    df['Low Similarity Mark'] = None
    df['ERGIN Score Details'] = None
    df['ERGIN Final Score'] = None

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Get the text from columns B and C
        standard_answer = row['B']
        user_answer = row['C']

        # Preprocess the text (remove punctuation, convert to lowercase, etc.)
        preprocessed_standard_answer = preprocess_text(standard_answer)
        preprocessed_user_answer = preprocess_text(user_answer)

        # Calculate the cosine similarity score
        similarity_score = cossim(preprocessed_standard_answer, preprocessed_user_answer)

        # Update the similarity score in the DataFrame
        df.loc[index, 'Similarity Score'] = similarity_score

        # Check for low similarity (below 0.8) and add a mark
        if similarity_score < 0.8:
            low_similarity_mark = 'Low Similarity'
        else:
            low_similarity_mark = None

        df.loc[index, 'Low Similarity Mark'] = low_similarity_mark

        # Score the user answer using ERGIN-3.5-8K
        ergin_score_details, ergin_final_score = score_using_ergin(standard_answer, user_answer)

        # Update the ERGIN score details and final score in the DataFrame
        df.loc[index, 'ERGIN Score Details'] = ergin_score_details
        df.loc[index, 'ERGIN Final Score'] = ergin_final_score

    # Save the updated DataFrame back to the Excel file
    df.to_excel(excel_file, index=False)

def preprocess_text(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Tokenize the text
    tokens = text.split()

    # Remove stop words
    stop_words = set(stopwords.words('chinese'))
    tokens = [token for token in tokens if token not in stop_words]

    # Join the tokens back into a string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

def score_using_ergin(standard_answer, user_answer):
    # Initialize the ERGIN-3.5-8K model
    ergin_model = ergin.ErginModel('ergin3.5-8k.bin')

    # Score the user answer against the standard answer
    ergin_score_details, ergin_final_score = ergin_model.evaluate(standard_answer, user_answer)

    return ergin_score_details, ergin_final_score

if __name__ == '__main__':
    excel_file = 'data.xlsx'  # Replace with the actual filename
    compare_similarity_and_score(excel_file)
