from arcgis.features import FeatureSet as _FeatureSet


feature_set = _FeatureSet.from_dict(_fs_dict)
data_frame = feature_set.sdf