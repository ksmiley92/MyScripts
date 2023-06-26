import arcpy
arcpy.analysis.Statistics("USDM_monthly_tab", r"C:\Drought_monitor_forage_loss\Drought_monitor_forage_loss2022.gdb\USDM_total_month", "Est_loss_cool SUM;Est_loss_warm SUM;Est_loss_mix SUM", "Month", '')
