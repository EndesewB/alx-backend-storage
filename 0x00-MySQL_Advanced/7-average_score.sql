-- Create a stored procedure to compute and store the average score for a user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2) DEFAULT 0;
    DECLARE total_projects INT DEFAULT 0;

    -- Calculate the total score and number of projects for the user
    SELECT SUM(score) INTO total_score, COUNT(*) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate and update the average score for the user
    IF total_projects > 0 THEN
        SET total_score = total_score / total_projects;
    END IF;

    UPDATE users
    SET average_score = total_score
    WHERE id = user_id;
END;

//
DELIMITER ;
