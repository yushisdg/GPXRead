
--高德数据插入触发器
CREATE OR REPLACE FUNCTION BeforeInsertGPXData() RETURNS TRIGGER AS $example_table$ 
BEGIN
--自动进行坐标计算，并赋值
NEW.geom=ST_PointFromText('POINT('||New.lon||' '||New.lat||')',4326);
return new;
End	;
$example_table$ LANGUAGE plpgsql;
CREATE TRIGGER BeforeInsertInsertGpxData_trigger Before INSERT  ON track_points_python FOR EACH ROW EXECUTE PROCEDURE BeforeInsertGPXData ();