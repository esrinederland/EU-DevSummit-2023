using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AddFeatures
{
    public sealed class SpatialReference : IEqualityComparer<SpatialReference>, IEquatable<SpatialReference>
    {
        [JsonProperty("wkid", NullValueHandling = NullValueHandling.Ignore)]
        public long? Wkid { get; set; }

        [DefaultValue(null)]
        [JsonProperty("latestWkid", NullValueHandling = NullValueHandling.Ignore)]
        public long? LatestWkid { get; set; }

        [DefaultValue(null)]
        [JsonProperty("xyTolerance", NullValueHandling = NullValueHandling.Ignore)]
        public double? XyTolerance { get; set; }

        [DefaultValue(null)]
        [JsonProperty("zTolerance", NullValueHandling = NullValueHandling.Ignore)]
        public double? ZTolerance { get; set; }

        [DefaultValue(null)]
        [JsonProperty("mTolerance", NullValueHandling = NullValueHandling.Ignore)]
        public double? MTolerance { get; set; }

        [DefaultValue(null)]
        [JsonProperty("falseX", NullValueHandling = NullValueHandling.Ignore)]
        public double? FalseX { get; set; }

        [DefaultValue(null)]
        [JsonProperty("falseY", NullValueHandling = NullValueHandling.Ignore)]
        public double? FalseY { get; set; }

        [DefaultValue(null)]
        [JsonProperty("xyUnits", NullValueHandling = NullValueHandling.Ignore)]
        public double? XyUnits { get; set; }

        [DefaultValue(null)]
        [JsonProperty("falseZ", NullValueHandling = NullValueHandling.Ignore)]
        public double? FalseZ { get; set; }

        [DefaultValue(null)]
        [JsonProperty("zUnits", NullValueHandling = NullValueHandling.Ignore)]
        public double? ZUnits { get; set; }

        [DefaultValue(null)]
        [JsonProperty("falseM", NullValueHandling = NullValueHandling.Ignore)]
        public double? FalseM { get; set; }

        [DefaultValue(null)]
        [JsonProperty("mUnits", NullValueHandling = NullValueHandling.Ignore)]
        public double? MUnits { get; set; }

        public SpatialReference() { }

        public SpatialReference(long wkid)
        {
            Wkid = wkid;
        }

        public override bool Equals(object obj)
        {
            if (obj is SpatialReference sr)
            {
                return sr.Wkid == Wkid;
            }

            return false;
        }

        public bool Equals(SpatialReference x, SpatialReference y)
        {
            return x.Wkid == y.Wkid;
        }

        public bool Equals(SpatialReference other)
        {
            return other.Wkid == Wkid;
        }

        public override int GetHashCode()
        {
            return Wkid.GetHashCode();
        }

        public int GetHashCode( SpatialReference obj)
        {
            return obj.Wkid.GetHashCode();
        }
    }
}