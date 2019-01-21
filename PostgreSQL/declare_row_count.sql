DO $$
DECLARE
	yr integer;
	a_count integer DEFAULT 0;
BEGIN
    yr := 2009;
	UPDATE sample_summary_umd s
	SET deforest_year = yr
	FROM (
	SELECT id, land_cover_90, ch1_year, first_clearing_type FROM sample_summary_UMD
	WHERE land_cover_90 LIKE 'Primary%'
	AND ch1_year = yr
	AND first_clearing_type LIKE '%leared%') as a
	WHERE s.id = a.id;
	GET DIAGNOSTICS a_count = ROW_COUNT;
	RAISE NOTICE 'The rows affected: %', a_count;
END $$;