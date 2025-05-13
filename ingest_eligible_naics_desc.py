import polars as pl
import duckdb
from dataclasses import dataclass


@dataclass
class LazyFrames:
    eligible_naics_desc: pl.LazyFrame = None
    for_book_rolls: pl.LazyFrame = None

    def __post_init__(self):
        self.eligible_naics_desc = (
            pl.read_excel(
                "eligible_naics_desc.xlsx", sheet_name="Eligible NAICS Descriptions"
            )
            .lazy()
            .select(
                [
                    pl.col("NAICS 2").cast(pl.UInt32).alias("naics2"),
                    pl.col("NAICS 3").cast(pl.UInt32).alias("naics3"),
                    pl.col("NAICS 4").cast(pl.UInt32).alias("naics4"),
                    pl.col("NAICS 5").cast(pl.UInt32).alias("naics5"),
                    pl.col("Full NAICS code").cast(pl.UInt32).alias("naics_cd"),
                    pl.col("description").alias("naics_desc"),
                    pl.col("eligible").cast(pl.UInt8).alias("is_eligible"),
                ]
            )
        )

        self.for_book_rolls = (
            pl.read_excel("eligible_naics_desc.xlsx", sheet_name="For Book Rolls")
            .lazy()
            .select(
                [
                    pl.col("NAICS 3").cast(pl.UInt32).alias("naics3"),
                    pl.col("NAICS 4").cast(pl.UInt32).alias("naics4"),
                    pl.col("NAICS 5").cast(pl.UInt32).alias("naics5"),
                    pl.col("NAICS Code").cast(pl.UInt32).alias("naics_cd"),
                    pl.col(r"% from Ask Kodiak")
                    .cast(pl.Float32)
                    .alias("pct_from_ask_kodiak"),
                    pl.col(r"% used for eligiblity")
                    .cast(pl.Float32)
                    .alias("pct_used_for_eligiblity"),
                    pl.col("BOP Eligible")
                    .cast(pl.Categorical)
                    .alias("is_eligible_for_bop"),
                    pl.col("SB Eligible")
                    .cast(pl.Categorical)
                    .alias("is_eligible_for_sb"),
                    pl.col("confirmed with Geyer's group")
                    .cast(pl.Categorical)
                    .alias("is_confirmed_with_geyers_group"),
                    pl.col("CLD Hit Ratio").cast(pl.Float32).alias("cld_hit_ratio"),
                    pl.col("CLD Declined Ratio")
                    .cast(pl.Float32)
                    .alias("cld_declined_ratio"),
                    pl.col("Submission Count").cast(pl.UInt32).alias("n_submissions"),
                    pl.col("NAICS Desc").cast(pl.Utf8).alias("naics_desc"),
                    pl.col("Key Questions").cast(pl.Utf8).alias("key_questions"),
                    pl.col("Unit Question").cast(pl.Utf8).alias("unit_question"),
                    pl.col("Program Question").cast(pl.Utf8).alias("program_question"),
                    pl.col("Associated BOP class codes")
                    .cast(pl.Utf8)
                    .alias("associated_bop_class_codes"),
                    pl.col("BOP class codes (vlookup)")
                    .cast(pl.Utf8)
                    .alias("bop_class_codes_vlookup"),
                ]
            )
        )


if __name__ == "__main__":
    lf = LazyFrames()
    lf1 = lf.eligible_naics_desc
    lf2 = lf.for_book_rolls

    with duckdb.connect("./naics.db") as c:
        c.sql("CREATE OR REPLACE TABLE eligible_naics AS (SELECT * FROM lf1)")
        c.sql("CREATE OR REPLACE TABLE for_book_rolls AS (SELECT * FROM lf2)")
