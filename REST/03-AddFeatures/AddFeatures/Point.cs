using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AddFeatures
{
    public class Point : IGeometry
    {
        [JsonProperty("x")]
        public double X { get; set; }

        [JsonProperty("y")]
        public double Y { get; set; }

        [DefaultValue(null)]
        [JsonProperty("z")]
        public double? Z { get; set; }

        [DefaultValue(null)]
        [JsonProperty("m")]
        public double? M { get; set; }

        [JsonProperty("spatialReference")]
        public SpatialReference SpatialReference { get; set; }

        [JsonIgnore]
        public string Type
        {
            get {
                return "esriGeometryPoint"; 
            }
        }

        public Point()
        { }

        public Point(int Wkid)
        {
            SpatialReference = new SpatialReference(Wkid);
        }

        public Point(SpatialReference spatialReference)
        {
            SpatialReference = spatialReference;
        }

        public Point( List<double> coordinates, SpatialReference spatialReference)
        {
            if (coordinates.Count >= 1)
            {
                X = coordinates[0];
            }

            if (coordinates.Count >= 2)
            {
                Y = coordinates[1];
            }

            if (coordinates.Count >= 3)
            {
                Z = coordinates[2];
            }

            if (coordinates.Count >= 4)
            {
                M = coordinates[3];
            }

            SpatialReference = spatialReference;
        }

        public override string ToString()
        {
            return Type;
        }
    }
}